# TypeScript examples

Each example shows the shape to avoid, then the shape to write. The rules are in [`../SKILL.md`](../SKILL.md).

## Inline single-use helpers

```ts
// Avoid. Three helpers, each called once. The reader jumps around to follow one story.
function sendInvoiceReminders(invoices: Invoice[], today: Date): void {
  const overdueInvoices = findOverdue(invoices, today);
  const messages = buildMessages(overdueInvoices);
  deliver(messages);
}

function findOverdue(invoices: Invoice[], today: Date): Invoice[] {
  return invoices.filter((invoice) => invoice.dueDate < today && !invoice.paid);
}

function buildMessages(invoices: Invoice[]): ReminderMessage[] {
  return invoices.map((invoice) => ({ to: invoice.customerEmail, invoiceId: invoice.id }));
}

function deliver(messages: ReminderMessage[]): void {
  for (const message of messages) {
    emailClient.send(message);
  }
}
```

```ts
// Write. One function that reads top to bottom. Blank lines split the steps.
function sendInvoiceReminders(invoices: Invoice[], today: Date): void {
  const overdueInvoices = invoices.filter((invoice) => invoice.dueDate < today && !invoice.paid);

  for (const invoice of overdueInvoices) {
    const reminderMessage = { to: invoice.customerEmail, invoiceId: invoice.id };
    emailClient.send(reminderMessage);
  }
}
```

## A deep module earns its extraction

```ts
// Write. Callers see one small function. The timeout, retries, backoff, and error mapping stay hidden behind it.
const customerApiTimeoutMs = 2_000;
const customerApiAttemptsMax = 3;
const retryDelayMsBase = 200;

export async function fetchCustomerProfile(customerId: string): Promise<CustomerProfile> {
  let lastError: unknown = null;

  for (let attempt = 1; attempt <= customerApiAttemptsMax; attempt++) {
    try {
      const response = await fetch(`${apiBaseUrl}/customers/${customerId}`, {
        signal: AbortSignal.timeout(customerApiTimeoutMs),
      });

      if (response.ok) {
        return parseCustomerProfile(await response.json());
      }

      if (response.status === 404) {
        throw new NotFoundError(`Customer ${customerId} not found`);
      }

      if (response.status < 500 && response.status !== 429) {
        throw new Error(`Customer API returned ${response.status}`);
      }

      lastError = new Error(`Customer API returned ${response.status}`);
    } catch (error) {
      if (!isNetworkOrTimeoutError(error)) {
        throw error;
      }
      lastError = error;
    }

    await waitMs(retryDelayWithJitterMs(attempt, retryDelayMsBase));
  }

  throw new UnavailableError("Customer API failed after retries", { cause: lastError });
}
```

`parseCustomerProfile`, `isNetworkOrTimeoutError`, `waitMs`, and `retryDelayWithJitterMs` are reused across the module, so they stay separate. A wrapper that only renamed `fetch` would not. A read is safe to retry. A write needs an idempotency key first (the **principle-assume-the-call-fails** skill).

## Guard clauses and the main path

```ts
// Avoid. The main path is buried three levels deep.
function applyDiscount(order: Order, discountCode: string | null): number {
  if (discountCode !== null) {
    const discount = discounts.get(discountCode);
    if (discount !== undefined) {
      if (!discount.expired) {
        return order.total * (1 - discount.percentage / 100);
      }
    }
  }
  return order.total;
}
```

```ts
// Write. Edge cases leave first. The main path sits at the left margin.
function applyDiscount(order: Order, discountCode: string | null): number {
  if (discountCode === null) {
    return order.total;
  }

  const discount = discounts.get(discountCode);
  if (discount === undefined || discount.expired) {
    return order.total;
  }

  return order.total * (1 - discount.percentage / 100);
}
```

## Simple over clever

```ts
// Avoid. Clever, short, and slow to read.
const totalsByCustomer = orders.reduce<Record<string, number>>(
  (accumulator, { customerId, total }) => ({ ...accumulator, [customerId]: (accumulator[customerId] ?? 0) + total }),
  {},
);
```

```ts
// Write. A plain loop says exactly what happens.
const totalsByCustomer = new Map<string, number>();

for (const order of orders) {
  const runningTotal = totalsByCustomer.get(order.customerId) ?? 0;
  totalsByCustomer.set(order.customerId, runningTotal + order.total);
}
```

```ts
// Avoid. Type gymnastics a reader has to evaluate in their head.
type EventHandlers<Events extends Record<string, unknown>> = {
  [EventName in keyof Events as `on${Capitalize<string & EventName>}`]: (payload: Events[EventName]) => void;
};
```

```ts
// Write. Spell out the shape.
type CheckoutEventHandlers = {
  onPaymentSucceeded: (payload: PaymentSucceeded) => void;
  onPaymentFailed: (payload: PaymentFailed) => void;
};
```

## Flag arguments

```ts
// Avoid. The boolean hides two different behaviors behind one name.
function exportReport(report: Report, asPdf: boolean): Uint8Array {
  if (asPdf) {
    return renderPdf(report);
  }
  return renderCsv(report);
}
```

```ts
// Write. The caller already knows which one it wants.
const pdfBytes = renderPdf(report);
const csvBytes = renderCsv(report);
```

## Names and one term per concept

```ts
// Avoid. Short names, and three words (user, account, member) for one concept.
function getAcct(uid: string): Account | undefined {
  const m = members.find((x) => x.userId === uid);
  return m?.account;
}
```

```ts
// Write. Long, plain names, and one word for the concept everywhere.
function findCustomerAccount(customerId: string): CustomerAccount | undefined {
  return customerAccounts.find((customerAccount) => customerAccount.customerId === customerId);
}
```

## Comments

```ts
// Avoid. Every comment repeats the code.
// Loop over the line items
for (const lineItem of order.lineItems) {
  // Add the price to the total
  orderTotalInCents += lineItem.priceInCents * lineItem.quantity;
}
```

```ts
// Write. No comment where the code is clear. One comment where the reason is not.
for (const lineItem of order.lineItems) {
  orderTotalInCents += lineItem.priceInCents * lineItem.quantity;
}

// The payment provider rejects charges below its minimum, so we waive them.
const chargeInCents = orderTotalInCents < providerMinimumChargeInCents ? 0 : orderTotalInCents;
```

## Assert what the types can't say

```ts
export function assert(condition: boolean, message: string): asserts condition {
  if (!condition) {
    throw new Error(`Assertion failed: ${message}`);
  }
}
```

```ts
// Write. The type says a number. The assertion says what the number must be.
function applyRefund(invoice: Invoice, refundInCents: number): Invoice {
  assert(refundInCents > 0, `refund must be positive, got ${refundInCents}`);
  assert(refundInCents <= invoice.paidInCents, `refund ${refundInCents} exceeds paid ${invoice.paidInCents}`);

  const refundedInvoice = { ...invoice, paidInCents: invoice.paidInCents - refundInCents };

  assert(refundedInvoice.paidInCents >= 0, "paid amount went negative");
  return refundedInvoice;
}
```

## Every limit is a named constant

```ts
// Avoid. Reads every page the API returns, however many there are.
let cursor: string | null = null;
do {
  const page = await listOrders({ cursor });
  orders.push(...page.orders);
  cursor = page.nextCursor;
} while (cursor !== null);
```

```ts
// Write. The limit has a name and a unit, and hitting it is an error, not a silent cut.
const orderPagesMax = 100;

let cursor: string | null = null;
for (let pageNumber = 1; pageNumber <= orderPagesMax; pageNumber++) {
  const page = await listOrders({ cursor });
  orders.push(...page.orders);
  cursor = page.nextCursor;

  if (cursor === null) {
    return orders;
  }
}

throw new Error(`Orders exceeded ${orderPagesMax} pages`);
```

## Errors translated at the boundary

```ts
// Avoid. The error disappears, and the caller gets an empty list as if nothing went wrong.
try {
  return await loadInvoices(customerId);
} catch (error) {
  logger.error({ error }, "failed to load invoices");
  return [];
}
```

```ts
// Write. Domain code throws a kind. The HTTP handler maps each kind once.
export class NotFoundError extends Error {
  readonly code = "not_found";
}

export class InvalidInputError extends Error {
  readonly code = "invalid_input";
}

function errorResponse(error: unknown): Response {
  if (error instanceof NotFoundError) {
    return Response.json({ error: { code: error.code, message: error.message } }, { status: 404 });
  }

  if (error instanceof InvalidInputError) {
    return Response.json({ error: { code: error.code, message: error.message } }, { status: 400 });
  }

  logger.error({ error }, "unhandled error");
  return Response.json({ error: { code: "internal", message: "Something went wrong" } }, { status: 500 });
}
```

## Plain functions over classes

```ts
// Avoid. A class with no state of its own.
class PriceFormatter {
  format(amountInCents: number, currency: string): string {
    return new Intl.NumberFormat("en-GB", { style: "currency", currency }).format(amountInCents / 100);
  }
}
```

```ts
// Write. A plain function.
export function formatPrice(amountInCents: number, currency: string): string {
  return new Intl.NumberFormat("en-GB", { style: "currency", currency }).format(amountInCents / 100);
}
```

## Section banners in a big file

```ts
// ------------------------------------------------------------
// Parsing
// ------------------------------------------------------------

export function parseCheckoutRequest(body: unknown): CheckoutRequest {
  // ...
}

// ------------------------------------------------------------
// Pricing
// ------------------------------------------------------------

export function priceCheckout(request: CheckoutRequest): PricedCheckout {
  // ...
}
```

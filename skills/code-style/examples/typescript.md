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
// Write. Callers see one small function. The retries, backoff, and error mapping stay hidden behind it.
export async function fetchCustomerProfile(customerId: string): Promise<CustomerProfile> {
  let lastError: unknown = null;

  for (let attempt = 1; attempt <= maximumAttempts; attempt++) {
    const response = await fetch(`${apiBaseUrl}/customers/${customerId}`);

    if (response.ok) {
      return parseCustomerProfile(await response.json());
    }

    if (response.status === 404) {
      throw new CustomerNotFoundError(customerId);
    }

    lastError = new Error(`Customer API returned ${response.status}`);
    await waitMilliseconds(attempt * retryDelayMilliseconds);
  }

  throw lastError;
}
```

`parseCustomerProfile` and `waitMilliseconds` are reused across the module, so they stay separate. A wrapper that only renamed `fetch` would not.

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
  orderTotal += lineItem.price * lineItem.quantity;
}
```

```ts
// Write. No comment where the code is clear. One comment where the reason is not.
for (const lineItem of order.lineItems) {
  orderTotal += lineItem.price * lineItem.quantity;
}

// The payment provider rejects amounts with more than two decimal places.
const chargeAmount = Math.round(orderTotal * 100) / 100;
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

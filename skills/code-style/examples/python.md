# Python examples

Each example shows the shape to avoid, then the shape to write. The rules are in [`../SKILL.md`](../SKILL.md).

## Inline single-use helpers

```python
# Avoid. Three helpers, each called once. The reader jumps around to follow one story.
def send_invoice_reminders(invoices: list[Invoice], today: date) -> None:
    overdue_invoices = _find_overdue(invoices, today)
    messages = _build_messages(overdue_invoices)
    _deliver(messages)


def _find_overdue(invoices: list[Invoice], today: date) -> list[Invoice]:
    return [invoice for invoice in invoices if invoice.due_date < today and not invoice.paid]


def _build_messages(invoices: list[Invoice]) -> list[ReminderMessage]:
    return [ReminderMessage(to=invoice.customer_email, invoice_id=invoice.id) for invoice in invoices]


def _deliver(messages: list[ReminderMessage]) -> None:
    for message in messages:
        email_client.send(message)
```

```python
# Write. One function that reads top to bottom. Blank lines split the steps.
def send_invoice_reminders(invoices: list[Invoice], today: date) -> None:
    overdue_invoices = [invoice for invoice in invoices if invoice.due_date < today and not invoice.paid]

    for invoice in overdue_invoices:
        reminder_message = ReminderMessage(to=invoice.customer_email, invoice_id=invoice.id)
        email_client.send(reminder_message)
```

## A deep module earns its extraction

```python
# Write. Callers see one small function. The retries, backoff, and error mapping stay hidden behind it.
def fetch_customer_profile(customer_id: str) -> CustomerProfile:
    last_error = None

    for attempt in range(1, MAXIMUM_ATTEMPTS + 1):
        response = http_client.get(f"{API_BASE_URL}/customers/{customer_id}")

        if response.status_code == 200:
            return parse_customer_profile(response.json())

        if response.status_code == 404:
            raise CustomerNotFoundError(customer_id)

        last_error = RuntimeError(f"Customer API returned {response.status_code}")
        time.sleep(attempt * RETRY_DELAY_SECONDS)

    raise RuntimeError(f"Customer API failed after {MAXIMUM_ATTEMPTS} attempts") from last_error
```

`parse_customer_profile` is reused across the module, so it stays separate. A wrapper that only renamed `http_client.get` would not.

## Guard clauses and the main path

```python
# Avoid. The main path is buried three levels deep.
def apply_discount(order: Order, discount_code: str | None) -> float:
    if discount_code is not None:
        discount = discounts.get(discount_code)
        if discount is not None:
            if not discount.expired:
                return order.total * (1 - discount.percentage / 100)
    return order.total
```

```python
# Write. Edge cases leave first. The main path sits at the left margin.
def apply_discount(order: Order, discount_code: str | None) -> float:
    if discount_code is None:
        return order.total

    discount = discounts.get(discount_code)
    if discount is None or discount.expired:
        return order.total

    return order.total * (1 - discount.percentage / 100)
```

## Simple over clever

```python
# Avoid. A walrus inside a nested comprehension. Short, and slow to read.
active_emails = [email for team in teams for member in team.members if (email := member.email) and member.active]
```

```python
# Write. A plain loop says exactly what happens.
active_emails = []

for team in teams:
    for member in team.members:
        if member.active and member.email:
            active_emails.append(member.email)
```

```python
# Avoid. Branching on a type through `match` patterns most readers have to look up.
def describe_payment(payment: Payment) -> str:
    match payment:
        case CardPayment(last_four=last_four):
            return f"Card ending {last_four}"
        case BankTransfer(reference=reference):
            return f"Bank transfer {reference}"
        case _:
            raise ValueError(f"Unknown payment: {payment!r}")
```

```python
# Write. Plain `if` and `isinstance`. The last line catches a case nobody handled.
def describe_payment(payment: Payment) -> str:
    if isinstance(payment, CardPayment):
        return f"Card ending {payment.last_four}"

    if isinstance(payment, BankTransfer):
        return f"Bank transfer {payment.reference}"

    raise ValueError(f"Unknown payment: {payment!r}")
```

## Flag arguments

```python
# Avoid. The boolean hides two different behaviors behind one name.
def export_report(report: Report, as_pdf: bool) -> bytes:
    if as_pdf:
        return render_pdf(report)
    return render_csv(report)
```

```python
# Write. The caller already knows which one it wants.
pdf_bytes = render_pdf(report)
csv_bytes = render_csv(report)
```

## Names and one term per concept

```python
# Avoid. Short names, and three words (user, account, member) for one concept.
def get_acct(uid: str) -> Account | None:
    m = next((x for x in members if x.user_id == uid), None)
    return m.account if m else None
```

```python
# Write. Long, plain names, and one word for the concept everywhere.
def find_customer_account(customer_id: str) -> CustomerAccount | None:
    for customer_account in customer_accounts:
        if customer_account.customer_id == customer_id:
            return customer_account

    return None
```

## Comments

```python
# Avoid. Every comment repeats the code.
# Loop over the line items
for line_item in order.line_items:
    # Add the price to the total
    order_total += line_item.price * line_item.quantity
```

```python
# Write. No comment where the code is clear. One comment where the reason is not.
for line_item in order.line_items:
    order_total += line_item.price * line_item.quantity

# The payment provider rejects amounts with more than two decimal places.
charge_amount = round(order_total, 2)
```

## Plain functions over classes

```python
# Avoid. A class with no state of its own.
class PriceFormatter:
    def format(self, amount_in_cents: int, currency: str) -> str:
        return f"{amount_in_cents / 100:.2f} {currency}"
```

```python
# Write. A plain function.
def format_price(amount_in_cents: int, currency: str) -> str:
    return f"{amount_in_cents / 100:.2f} {currency}"
```

## Section banners in a big file

```python
# ------------------------------------------------------------
# Parsing
# ------------------------------------------------------------


def parse_checkout_request(body: dict[str, object]) -> CheckoutRequest:
    ...


# ------------------------------------------------------------
# Pricing
# ------------------------------------------------------------


def price_checkout(request: CheckoutRequest) -> PricedCheckout:
    ...
```

# TypeScript patterns

Examples for the rules in `../SKILL.md`. Style examples (inlining, names, layout, comments) live in the **code-style** skill.

## Parse at the boundary

```ts
import { z } from "zod";

const createUserRequestSchema = z.object({
  email: z.string().email(),
  displayName: z.string().min(1),
});

type CreateUserRequest = z.infer<typeof createUserRequestSchema>;

function parseCreateUserRequest(body: unknown): CreateUserRequest {
  return createUserRequestSchema.parse(body);
}
```

Use the schema library the repo already has. Don't add one for a single check.

## Plain discriminated unions and an exhaustive `switch`

```ts
// Avoid. Optional fields allow states that can't happen, such as loading with an error.
type UploadState = { loading: boolean; fileUrl?: string; errorMessage?: string };
```

```ts
// Write. Each state carries only its own data.
type UploadState =
  | { kind: "uploading" }
  | { kind: "uploaded"; fileUrl: string }
  | { kind: "failed"; errorMessage: string };

function describeUpload(uploadState: UploadState): string {
  switch (uploadState.kind) {
    case "uploading":
      return "Uploading";
    case "uploaded":
      return `Uploaded to ${uploadState.fileUrl}`;
    case "failed":
      return `Upload failed: ${uploadState.errorMessage}`;
    default:
      throw new Error(`Unknown upload state: ${JSON.stringify(uploadState)}`);
  }
}
```

## No `as` and no `!`

```ts
// Avoid. Both lines claim something the compiler can't check.
const settings = JSON.parse(rawSettings) as Settings;
const firstOrder = orders[0]!;
```

```ts
// Write. Parse the data, and handle the missing value.
const settings = settingsSchema.parse(JSON.parse(rawSettings));

const firstOrder = orders[0];
if (firstOrder === undefined) {
  return null;
}
```

## Spell types out

```ts
// Avoid. The reader has to run the type in their head.
type Nullable<T> = { [Key in keyof T]: T[Key] | null };
type DraftInvoice = Nullable<Pick<Invoice, "customerId" | "dueDate">>;
```

```ts
// Write.
type DraftInvoice = {
  customerId: string | null;
  dueDate: Date | null;
};
```

## Object parameters past three

```ts
// Avoid. Easy to swap two numbers and still compile.
scheduleReminder(customerId, 3, 9, true);
```

```ts
// Write.
scheduleReminder({ customerId, daysBeforeDueDate: 3, sendAtHour: 9 });
```

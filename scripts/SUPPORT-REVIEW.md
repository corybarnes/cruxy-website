# Support pages: statements to confirm before launch

Written from a read of the app code. Check each against the live app or your own knowledge.

- Billing > Receipts: assumes Stripe's billing page shows payment history and receipts. Confirm in the Stripe customer portal settings.
- Billing > Manage subscription: assumes the Stripe portal lets people update their card and cancel (it is what "Manage Subscription" opens).
- Billing > Cancel: says Pro continues to the end of the paid period. The app banner ("Your Pro plan ends ...") implies this.
- Alerts > Wording: says replies from clients go to the business email, or the login email if none. Confirmed for the test email; confirm for the nightly sender.
- Alerts > Overdue: the alert email itself is a Klaviyo flow that is not built yet. The page describes its contents (invoice, client, amount, days overdue, whether the client was reminded) as the data we send.
- Alerts > Client reminders: waits for the client-reminders branch to be merged and its UI final.
- Free vs Pro > If Pro ends: says retainers pause and budgets stay but cannot change (from the app code); confirm client reminders stop for Free workspaces.
- Account > Install: iPhone and Android steps are standard browser steps. Check on a real device.
- Invoices > Share: "sharing an unsent invoice marks it sent" is from the share code. Whether Download also marks an invoice sent is not confirmed, so the pages do not say it does.
- Time > Timer: says a running timer can be stopped from another device (from the multi-device sync code).
- Get started > Create account: Google sign-up is not offered to new people (decision), so the page does not mention it.

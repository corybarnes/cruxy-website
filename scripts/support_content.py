# Content for the Cruxy support section. Run scripts/build_support.py to regenerate the pages.
# Each page: slug, title, desc, intro, sections. A section is (id, title, html, shots, [kind]).
# A shot is (image path under images/ or None, alt text, "what the missing screenshot should show").
# Shots whose image file is missing render as a placeholder and are listed in scripts/SCREENSHOTS.md.

S = 'support/'   # images/support/
A = 'app/'       # images/app/

def shot(path, alt, need=''):
    return (path, alt, need)

PAGES = []

# ---------------------------------------------------------------- Get started
PAGES.append(dict(
    slug='get-started', title='Get started', nav='Get started',
    desc='Set up Cruxy in about five minutes: create your account, add your business details and first client, log your first time and send your first invoice.',
    intro='Cruxy tracks your time and turns it into invoices. Setup takes about five minutes.',
    sections=[
    ('create-account', 'Create your account', '''
<ol>
<li>Go to <a href="https://get.cruxy.io/signup">get.cruxy.io/signup</a>.</li>
<li>Enter your name, email and a password (at least 6 characters). Add your business or agency name if you like. We use your name if you leave it blank.</li>
<li>Tick the box to agree to the Terms and Privacy Policy.</li>
<li>Tap <strong>Create Account</strong>.</li>
<li>If we ask you to confirm your email, open the message we sent, tap the link, then sign in.</li>
</ol>
<p class="note">Cruxy is free to start. You don't need a credit card.</p>
<p>You can use Cruxy on the web at get.cruxy.io, or add it to your phone's home screen so it opens like an app. See <a href="../account/#install">Install Cruxy on your phone</a>.</p>''',
     [shot(S+'signup.png', 'The Cruxy Create your account form, filled in with example details')], 'step'),
    ('business-details', 'Add your business details', '''
<p>Tap your avatar in the top right, then the gear icon to open Settings. Choose the <strong>Invoicing</strong> tab and fill in:</p>
<ul>
<li>Your business address and email, which appear on your invoices</li>
<li>Payment instructions, such as bank details or a payment link</li>
<li>Payment terms: Due on receipt, Net 15 or Net 30</li>
<li>Your tax label and rate, if you charge tax</li>
<li>A logo (PNG or JPG, up to 2 MB), if you want one</li>
</ul>
<p>Tap <strong>Save</strong>. You can change any of this later. Changes apply to invoices you create afterward, not ones you've already made.</p>''',
     [shot(S+'settings-invoicing.png', 'The Invoicing tab in Cruxy Settings with business address, payment instructions, terms and tax')], 'step'),
    ('first-client', 'Add your first client', '''
<ol>
<li>Tap <strong>Clients</strong>, then <strong>New</strong>.</li>
<li>Enter the client's name and a first project, for example "Website redesign".</li>
<li>Choose a currency and enter your hourly rate. A rate of 0 makes the client non-billable.</li>
<li>Pick a color, then tap <strong>Add Client</strong>.</li>
</ol>
<p>To send invoices by email, add a billing email. Tap the client, then the gear icon next to the name to open the details.</p>''',
     [shot(None, 'The New client form in Cruxy', 'The New client sheet: client name, first project, currency, hourly rate and color')], 'step'),
    ('first-time', 'Log your first time', '''
<p><strong>With the timer</strong></p>
<ol>
<li>Tap <strong>Timer</strong> and pick the client, project and task.</li>
<li>Tap <strong>Start Timer</strong>. Tap <strong>Pause</strong> if you take a break.</li>
<li>Tap <strong>Stop &amp; Log</strong> when you're done. The time is saved as an entry, rounded to the nearest minute.</li>
</ol>
<p><strong>By hand</strong></p>
<p>Tap <strong>Entries</strong>, then <strong>New</strong>, then <strong>Time Entry</strong>. Enter the date, hours and minutes.</p>''',
     [shot(A+'app-timer.jpg', 'The Cruxy timer running for a client, project and task'), shot(S+'new-entry.png', 'The New entry form in Cruxy')], 'step'),
    ('first-invoice', 'Send your first invoice', '''
<ol>
<li>Tap <strong>Clients</strong>, then the client, then the <strong>Invoices</strong> tab.</li>
<li>Tap <strong>New Invoice</strong> and choose the period.</li>
<li>Check the invoice number, dates and terms. Add a discount or a note if you need one, and untick any fees you want to leave off.</li>
<li>Tap <strong>Create Invoice</strong>.</li>
<li>Tap the email icon to send it as a PDF. You can also tap Share or Download and send it yourself.</li>
</ol>
<p class="note">Free includes 3 emailed invoices a month. Sharing and downloading are always free. When you email or share an invoice, Cruxy marks it as sent.</p>''',
     [shot(S+'new-invoice.png', 'The New Invoice sheet in Cruxy with period, tax and total'), shot(S+'email-invoice.png', 'The Email invoice sheet in Cruxy')], 'step'),
    ]))

# ---------------------------------------------------------------- Logging time
PAGES.append(dict(
    slug='time', title='Logging time', nav='Logging time',
    desc='How to use the Cruxy timer, add and edit time entries, use the timesheet, filter entries, work offline and export your hours.',
    intro='Track time with the timer, add it by hand, or fill in a weekly timesheet.',
    sections=[
    ('timer', 'Use the timer', '''
<ol>
<li>Tap <strong>Timer</strong>. Pick the client, project and task.</li>
<li>Tap <strong>Start Timer</strong>.</li>
<li>Tap <strong>Pause</strong> for a break and <strong>Resume</strong> to carry on.</li>
<li>Tap <strong>Stop &amp; Log</strong> to save the time as an entry.</li>
</ol>
<p>Time is rounded to the nearest minute, with a minimum of 1 minute. Paused time isn't counted. The pickers are locked while the timer runs.</p>
<p>A running timer survives closing the app. If you start it on your phone, you can stop it from another device.</p>''',
     [shot(A+'app-timer.jpg', 'The Cruxy timer running')]),
    ('manual-entry', 'Add a time entry by hand', '''
<ol>
<li>Tap <strong>Entries</strong>, then <strong>New</strong>, then <strong>Time Entry</strong>.</li>
<li>Choose the date, client, project and task.</li>
<li>Enter the hours and minutes. Add a note if you like.</li>
<li>Tap <strong>Add Entry</strong>.</li>
</ol>
<p>The smallest entry is 1 minute.</p>''',
     [shot(S+'new-entry.png', 'The New entry form')]),
    ('edit-entry', 'Edit or delete an entry', '''
<p>Tap an entry in Entries (or in "Your entries today" on the Timer) to open it. Change what you need and tap <strong>Save Changes</strong>. To remove it, tap the trash icon and confirm. Deleting can't be undone.</p>
<p>A few things to know:</p>
<ul>
<li>Entries for an archived client are view only.</li>
<li>If the time is already on an invoice, a note tells you which one. You can still edit or delete the entry, but the invoice does not change.</li>
<li>Each entry keeps the rate it was logged at. If you change a client's rate later, old entries keep their original rate. Tap <strong>Use Current Rate</strong> on an entry to switch it.</li>
</ul>''', []),
    ('rate', 'Change the rate on a single entry', '''
<p>If the client has an hourly rate, the timer and the entry form show a rate row. Tap it to choose <strong>Default Rate</strong>, <strong>Custom Rate</strong> (an hourly rate you type in) or <strong>Non-Billable</strong>. Non-billable time never goes on an invoice.</p>''', []),
    ('resume', 'Resume an earlier entry', '''
<p>In "Your entries today" on the Timer, tap <strong>Resume</strong> on an entry. The timer starts, and when you stop it the time is added to that entry. If another timer is running, it is logged first.</p>''', []),
    ('timesheet', 'Use the weekly timesheet', '''
<p>On <strong>Entries</strong>, switch to <strong>Timesheet view</strong> to see the week as a grid, one card per client.</p>
<ul>
<li><strong>Add Row</strong> picks a client, project and task to list.</li>
<li><strong>Copy Last Week's Rows</strong> brings over last week's rows (not the time) to save setup.</li>
<li>Tap an empty cell and type a time such as <code>1h 30m</code>, <code>1:30</code>, <code>1.5</code> or <code>90m</code>. The most you can add at once is 24 hours.</li>
<li>Tap a cell that already has time to edit it. A cell with several entries opens a list.</li>
</ul>
<p>The week starts on the day you choose in <a href="../account/#profile">Settings &gt; Profile</a>.</p>''',
     [shot(S+'timesheet-phone.png', 'The weekly timesheet in Cruxy')]),
    ('filter', 'Filter your entries', '''
<p>On Entries, tap the filter button (sliders icon). You can show:</p>
<ul>
<li><strong>Unbilled</strong> or <strong>Billed</strong> time</li>
<li>Time, fixed fees or expenses</li>
<li>One or more clients, including archived clients</li>
</ul>
<p>The client filter also applies to the Summary tab.</p>''',
     [shot(S+'filter-entries.png', 'The Filter entries sheet')]),
    ('period', 'Change the period you are viewing', '''
<p>The bar at the top of Entries and Summary switches between <strong>Week</strong>, <strong>Month</strong> and <strong>Custom</strong>. Use the arrows to step to the previous or next period, and the double arrow to jump back to today. Both tabs share the same period.</p>''', []),
    ('summary', 'See your totals on Summary', '''
<p>The <strong>Summary</strong> tab shows hours, what you earned, and any fixed fees and expenses for the period, a chart by day or week, and breakdowns by client and by task. Amounts are shown per currency.</p>''',
     [shot(A+'app-summary.jpg', 'The Cruxy Summary tab')]),
    ('export', 'Export your time', '''
<p>On Summary, tap the download icon.</p>
<ul>
<li><strong>Export CSV</strong> saves every entry in the period: date, client, project, task, hours, rate, earnings, currency, whether it's billable, invoice number and note.</li>
<li><strong>Export PDF</strong> saves a summary for the period with one section per client.</li>
</ul>
<p>Free PDFs carry a small "Generated with Cruxy" credit. Pro PDFs don't.</p>''', []),
    ('tasks', 'Manage your tasks', '''
<p>Tasks (like Design or Meetings) are shared across all your clients. Open <strong>Settings &gt; Tasks</strong> to add, rename or delete them.</p>
<ul>
<li>You can also add a task from the Timer's task list with <strong>+ Add task</strong>.</li>
<li>Renaming a task changes its name on every entry, including old ones.</li>
<li>You can't delete a task that has entries. Rename it instead.</li>
</ul>''',
     [shot(S+'settings-tasks.png', 'The Tasks tab in Settings')]),
    ('offline', 'Work offline', '''
<p>New time entries are saved on your device first, then sent when you're online. A banner shows when entries are waiting to sync and confirms when everything is saved.</p>
<p>Editing or deleting entries, and anything in Clients, Settings and invoices, needs a connection. If an entry can't be saved (for example, its client was deleted), the banner offers <strong>Retry</strong> or <strong>Discard</strong>.</p>''', []),
    ]))

# ---------------------------------------------------------------- Clients and projects
PAGES.append(dict(
    slug='clients-projects', title='Clients and projects', nav='Clients and projects',
    desc='Add clients and projects in Cruxy, set rates and currencies, archive clients, import from Clockify, Toggl or Harvest, and add fixed fees and expenses.',
    intro='Clients and projects organize your time and decide what you charge.',
    sections=[
    ('add-client', 'Add a client', '''
<ol>
<li>Tap <strong>Clients</strong>, then <strong>New</strong>.</li>
<li>Enter the client's name and a first project.</li>
<li>Choose a currency and your hourly rate. A rate of 0 makes the client non-billable, so no invoices can be made for them.</li>
<li>Pick a color and tap <strong>Add Client</strong>.</li>
</ol>
<p>Free includes 2 active clients. Archive one you're finished with, or <a href="../free-vs-pro/">go Pro</a> for unlimited.</p>''',
     [shot(A+'app-clients.jpg', 'The Cruxy Clients list')]),
    ('client-details', 'Edit a client\'s details', '''
<p>Tap a client, then the gear icon next to the name. You can change:</p>
<ul>
<li>Name, currency, hourly rate and color</li>
<li>Billing name, email and address. These appear on the invoice, and the email is where invoices are sent.</li>
<li>A tax rate for this client, if different from your default</li>
<li>How invoice time is rounded for this client</li>
</ul>
<p>Changing the hourly rate affects future entries only. Past entries keep the rate they were logged at.</p>
<p>You can't change a client's currency while it has unbilled time or charges. Invoice them or remove them first. Changing the currency doesn't convert the rate, so update it too.</p>''',
     [shot(S+'client-details.png', 'A client\'s details in Cruxy')]),
    ('projects', 'Add and edit projects', '''
<p>Tap a client, then the <strong>Projects</strong> tab.</p>
<ul>
<li>Type a name in the box and tap <strong>Add</strong> to create a project.</li>
<li>Tap a project to rename it, give it its own hourly rate, or archive it.</li>
<li><strong>View archived projects</strong> shows the ones you've put away. Archived projects don't appear when you log time, but their old entries stay.</li>
</ul>
<p>A project rate replaces the client's rate for that project. Leave it blank to use the client's rate. A project can't make a non-billable client billable.</p>''',
     [shot(S+'client-projects.png', 'The Projects tab for a client')]),
    ('archive', 'Archive and unarchive a client', '''
<p>Archive a client when the work is done. In the client's details, tap <strong>Archive</strong> and confirm.</p>
<ul>
<li>Archived clients are hidden from the timer and pickers and become read-only.</li>
<li>Their time, projects and invoices stay. You can still invoice unbilled time and mark invoices paid.</li>
<li>Archived clients don't count toward your 2 active clients on Free.</li>
</ul>
<p>To bring one back, tap <strong>Show Archived Clients</strong> on the Clients tab, then <strong>Unarchive</strong>. On Free you need a free slot first, so archive another client or go Pro.</p>''', []),
    ('delete-client', 'Delete a client', '''
<p>Deleting a client permanently deletes its projects and all of its time entries. It can't be undone. If you might need the history, archive the client instead.</p>''', []),
    ('charges', 'Add a fixed fee or expense', '''
<p>Use a charge for something that isn't hourly, like a flat fee or a purchase you're passing on.</p>
<ol>
<li>Tap <strong>Entries</strong>, then <strong>New</strong>, then <strong>Charge</strong>.</li>
<li>Choose the client and date, and whether it's a <strong>Fixed Fee</strong> or an <strong>Expense</strong>.</li>
<li>Add a description and amount. Turn <strong>Taxable</strong> off if your invoice tax shouldn't apply to it.</li>
<li>Tap <strong>Add Charge</strong>.</li>
</ol>
<p>Unbilled charges appear on your next invoice for that client. A charge that's already on an invoice can't be edited. Delete the invoice first. The client needs an hourly rate above 0 to get charges.</p>''',
     [shot(S+'new-charge.png', 'The New charge sheet')]),
    ('import', 'Import from Clockify, Toggl or Harvest', '''
<p>Switching from another tracker? Import your time from its CSV export. Import is free on every plan.</p>
<ol>
<li>Export your time entries as a CSV from Clockify, Toggl or Harvest.</li>
<li>In Cruxy, tap <strong>Clients</strong>, then <strong>Import</strong>, then <strong>Choose CSV</strong>.</li>
<li>Review the summary: the entries, the date range, and which clients are new or existing.</li>
<li>Tap <strong>Import</strong>.</li>
</ol>
<p>Every row needs a date, a duration and a client. Entries already in Cruxy are skipped, so importing the same file twice is safe. If any rows can't be read, nothing is imported until you fix the file. The file can be up to 10 MB.</p>
<p>On Free, new clients beyond your 2 active clients are imported as archived. You can choose which to keep active, or go Pro.</p>
<p>Right after an import, tap <strong>Undo Import</strong> if you need to take it back. Once you close that screen, the option is gone.</p>''',
     [shot(A+'import-pick.jpg', 'Choosing a CSV file to import'), shot(A+'import-review.png', 'Reviewing an import before it runs')]),
    ('choose-clients', 'If Cruxy asks you to choose clients', '''
<p>If a Free workspace has more than 2 active clients, for example after Pro ends, Cruxy asks you to pick the 2 to keep active. The others are archived with their data kept. You can't log new time until you choose. Going Pro again lifts the limit.</p>''',
     [shot(None, 'The Choose clients to keep active sheet', 'The "Choose clients to keep active" sheet with two clients ticked')]),
    ]))

# ---------------------------------------------------------------- Invoices
PAGES.append(dict(
    slug='invoices', title='Invoices', nav='Invoices',
    desc='Create, email, share, download and manage invoices in Cruxy. Mark invoices sent or paid, send a reminder, and understand overdue status.',
    intro='Turn your unbilled time into a PDF invoice and send it from the app.',
    sections=[
    ('create', 'Create an invoice', '''
<ol>
<li>Tap <strong>Clients</strong>, then the client, then the <strong>Invoices</strong> tab.</li>
<li>Tap <strong>New Invoice</strong> and choose the period: last month, this month or a custom range.</li>
<li>Check the <strong>invoice number</strong> (we suggest the next one), the issue date and the payment terms.</li>
<li>Set the tax rate, and add a discount or a note if you need to.</li>
<li>Under <strong>Fees and expenses</strong>, untick any charge you want to leave off, or tap <strong>Add Charge</strong>.</li>
<li>Tap <strong>Create Invoice</strong>.</li>
</ol>
<p>The client needs an hourly rate above 0 to be invoiced. The Invoices tab also shows how much is unbilled.</p>''',
     [shot(S+'client-invoices.png', 'A client\'s Invoices tab'), shot(S+'new-invoice.png', 'The New Invoice sheet')]),
    ('contents', 'What goes on an invoice', '''
<ul>
<li>Billable time in the period. Non-billable entries stay off, and so does time already on another invoice.</li>
<li>Lines are grouped by project, task and rate. If a rounding setting applies, each line is rounded, not each entry.</li>
<li>Tax applies to time and to any taxable charges. A discount comes off before tax.</li>
<li>If the period has time in more than one currency, Cruxy asks you to invoice them separately.</li>
</ul>
<p>An invoice is a snapshot. Later changes to the client, your settings or the entries don't change it. If you need a change, delete the invoice and create it again.</p>
<p>If the period has nothing to invoice, Cruxy says so and doesn't make an invoice.</p>''', []),
    ('view', 'View an invoice', '''
<p>Tap an invoice in the client's list to see Bill To, the lines, the totals, your payment instructions and notes. The status shows as <strong>Not sent</strong>, <strong>Sent</strong>, <strong>Overdue</strong> or <strong>Paid</strong>.</p>''',
     [shot(A+'invoices-list.png', 'A client\'s invoices with paid and overdue statuses')]),
    ('email', 'Email an invoice', '''
<ol>
<li>Open the invoice and tap the email icon.</li>
<li>Check the <strong>To</strong> address. It comes from the client's billing email.</li>
<li>Edit the subject and message if you like. A copy to yourself is on by default.</li>
<li>Tap <strong>Send Invoice</strong>.</li>
</ol>
<p>The invoice goes as a PDF attachment. Replies come to you. Emailing marks the invoice as sent.</p>
<p>Free includes 3 emailed invoices or reminders a month, renewing on the 1st. Pro has no monthly limit. See <a href="../free-vs-pro/">Free vs Pro</a>.</p>''',
     [shot(S+'email-invoice.png', 'The Email invoice sheet')]),
    ('share-download', 'Share or download an invoice', '''
<p>Tap <strong>Download</strong> to save the PDF, or <strong>Share</strong> to send it with your phone's share sheet (on devices that support it). Sharing and downloading are free and unlimited. Sharing an unsent invoice marks it as sent.</p>
<p>Free invoices carry a small "Generated with Cruxy" line at the bottom. Pro invoices don't. If you've uploaded a logo, it's included.</p>''', []),
    ('status', 'Mark an invoice sent or paid', '''
<ul>
<li><strong>Mark as Sent</strong> when you've sent it yourself.</li>
<li><strong>Mark as Paid</strong> when the money arrives. A message offers <strong>Undo</strong> in case you tapped it by mistake.</li>
<li><strong>Mark as Unpaid</strong> or <strong>Mark as Unsent</strong> reverses the status.</li>
<li>Tap the underlined sent or paid date to change it.</li>
</ul>
<p>An invoice is <strong>Overdue</strong> when it's been sent, isn't paid and is past its due date. An invoice due on receipt gets one business day before it counts as overdue.</p>
<p>Cruxy doesn't take payments from your clients. You get paid however your payment instructions say.</p>''', []),
    ('reminder', 'Send a reminder for an overdue invoice', '''
<p>Open an overdue invoice and tap the email icon. Switch to <strong>Reminder</strong>, check the message and tap <strong>Send Reminder</strong>. A manual reminder counts toward your free monthly emails.</p>
<p>Pro can send reminders automatically. See <a href="../alerts/#client-reminders">Automatic reminders to your clients</a>.</p>''', []),
    ('delete', 'Delete an invoice', '''
<p>Open the invoice and tap <strong>Delete</strong>. The time and charges on it count as unbilled again. This can't be undone, and there's no void. Deleting doesn't unsend an email your client already received.</p>
<p>Invoices can't be edited after they're created. To change one, delete it and make a new one.</p>''', []),
    ]))

# ---------------------------------------------------------------- Alerts
PAGES.append(dict(
    slug='alerts', title='Alerts', nav='Alerts',
    desc='Set up Cruxy alerts: a reminder to log your time, overdue invoice alerts to you, and automatic payment reminders to your clients on Pro.',
    intro='Cruxy can nudge you to log time, tell you when an invoice is overdue, and on Pro remind your clients for you.',
    sections=[
    ('overview', 'Where to find them', '''
<p>Open <strong>Settings &gt; Alerts</strong>. There are three switches, and all start off:</p>
<ul>
<li><strong>Remind Me to Log Time</strong> (Free and Pro)</li>
<li><strong>Send Me Overdue Invoice Alerts</strong> (Free and Pro)</li>
<li><strong>Send My Clients Overdue Invoice Alerts</strong> (Pro)</li>
</ul>
<p>Each has a <strong>Customize</strong> link for the details. Flipping a switch saves it right away.</p>''',
     [shot(None, 'The Alerts tab in Settings with three switches', 'Settings > Alerts with the three switches (one on, two off), Customize links visible')]),
    ('log-time', 'Remind me to log time', '''
<p>Turn on <strong>Remind Me to Log Time</strong> and Cruxy emails you at a time you choose, on the days you choose, as long as you haven't logged any time yet that day. Tap <strong>Customize</strong> to set <strong>Email Me At</strong> (any hour from 5:00 AM to 10:00 PM) and the days of the week. The default is 5:00 PM, Monday to Friday.</p>
<p>The time uses the time zone of the device you saved it on.</p>''',
     [shot(None, 'The Remind Me to Log Time sheet', 'The Customize sheet for the log-time reminder: time picker and day buttons')]),
    ('overdue', 'Overdue invoice alerts to you', '''
<p>Turn on <strong>Send Me Overdue Invoice Alerts</strong> and Cruxy emails you when a sent invoice is still unpaid. Tap <strong>Customize</strong> to choose when: <strong>When Overdue</strong> (the day it becomes overdue), <strong>1 Week</strong>, <strong>30 Days</strong> and <strong>60 Days</strong> after.</p>
<p>Each alert lists the invoice, the client, the amount and how many days it is overdue. It also says whether your client has been reminded.</p>
<p>An invoice counts as overdue once it's been sent, isn't paid and is past its due date. Due-on-receipt invoices get one business day first.</p>''',
     [shot(None, 'The Overdue Invoice Alerts sheet', 'The Customize sheet for overdue alerts with the four timing chips')]),
    ('client-reminders', 'Automatic reminders to your clients (Pro)', '''
<p>With Pro, Cruxy can email your client for you when an invoice is overdue. It goes out from your business name, so it reads like it came from you.</p>
<ol>
<li>Open <strong>Settings &gt; Alerts</strong> and turn on <strong>Send My Clients Overdue Invoice Alerts</strong>.</li>
<li>Tap <strong>Customize</strong> to see a preview of the email and choose its wording.</li>
</ol>
<p>When this is on, every active client gets reminders on the day an invoice becomes overdue, and again at 7 and 30 days. Clients with no billing email are skipped. Add one in the client's details. Nothing is sent for an invoice that has been paid.</p>''',
     [shot(None, 'The Client Alerts sheet with a preview', 'The Customize sheet for client alerts: preview, Write My Own, Send Me a Test, Save')]),
    ('wording', 'Choose what the email says', '''
<p>The default message is friendly and short: it says the invoice is past due, thanks them if they have already paid, and invites them to reply with questions.</p>
<p>To write your own, tap <strong>Write My Own</strong> and type up to 1,000 characters of plain text. Tap <strong>Use Default</strong> to go back. Cruxy always adds the greeting, the invoice details (number, amount, due date and days overdue), your payment instructions and a thank-you. The subject is also written for you, for example "Reminder: Invoice 1042 from Acme is 7 days past due".</p>
<p>Tap <strong>Send Me a Test</strong> to get a sample at your own email address. It's never sent to a client. Replies from clients go to your business email, or to your login email if you haven't set one.</p>''',
     [shot(None, 'An example reminder email as the client sees it', 'The reminder email in an inbox: subject, greeting, standard message, invoice details table, How to pay box, thank-you')]),
    ('per-client', 'Change reminders for one client', '''
<p>Open a client and tap the <strong>Reminders</strong> tab. Switch reminders off for just that client, or tap <strong>Customize</strong> to pick which days they get a reminder: When Overdue, 1 Week, 30 Days or 60 Days. If client reminders are off in Settings, this tab says so and offers a shortcut to turn them on.</p>''',
     [shot(None, 'The Reminders tab for a client', 'A client\'s Reminders tab with the switch and Customize link')]),
    ('status', 'See who has been reminded', '''
<p>Open an overdue invoice. Under the title you'll see "Client reminded" with the date and the number sent, or a note if a reminder didn't arrive or was marked as spam. The overdue alert email you get also says whether the client was notified.</p>''', []),
    ]))

# ---------------------------------------------------------------- Budgets and retainers
PAGES.append(dict(
    slug='budgets-retainers', title='Budgets and retainers', nav='Budgets and retainers',
    desc='Set project budgets with monthly rollover and a heads-up at 80%, and bill retainers on a schedule with Cruxy Pro.',
    intro='Project budgets and retainers are Pro features. They help you stay on scope and bill recurring work.',
    sections=[
    ('budget', 'Set a project budget', '''
<ol>
<li>Tap <strong>Clients</strong>, then the client, then the <strong>Projects</strong> tab.</li>
<li>Tap a project.</li>
<li>Under <strong>Budget</strong>, choose <strong>Hours</strong> or <strong>Amount</strong> and enter the number.</li>
<li>Choose the <strong>Period</strong>: the whole project, each month or each week.</li>
<li>Tap <strong>Save</strong>.</li>
</ol>
<p>A progress bar on the project shows how much is used, for example "26.5 of 40 hrs". Budgets count billable time for the whole workspace.</p>''',
     [shot(S+'project-budget.png', 'The Edit project sheet with a budget')]),
    ('heads-up', 'The 80% heads-up', '''
<p>When logged time takes a project to 80% of its budget, Cruxy shows a heads-up. It shows another when the project goes over. The bar changes color at those points.</p>''', []),
    ('rollover', 'Roll over unused budget', '''
<p>For a monthly budget, turn on <strong>Roll Over Unused Hours</strong> (or <strong>Budget</strong>). Unused budget carries into the next month, up to one month's worth, and overspending comes out of next month. The balance starts from the first of the current month and restarts if you change the budget.</p>
<p>Weekly budgets follow the week start day set on each device.</p>''', []),
    ('retainer', 'Bill a retainer', '''
<p>A retainer is a fixed fee that repeats. Cruxy adds the charge on each date, ready to go on your next invoice.</p>
<ol>
<li>Tap a client, then the gear icon for details.</li>
<li>Tap <strong>Add a fixed fee that repeats</strong> under Retainer.</li>
<li>Enter a description and amount, and choose how often it repeats (monthly, weekly, every 2 weeks or quarterly) and on which day.</li>
<li>Set the start date, and an end date if you want one.</li>
<li>Tap <strong>Save Retainer</strong>.</li>
</ol>
<p>Each client can have one retainer. The row shows the next charge date, or that it's paused or ended. Charges appear in Entries like any fixed fee, and the Invoices tab shows how many are ready to invoice.</p>''',
     [shot(S+'retainer.png', 'The Retainer sheet'), shot(A+'retainers-progress.png', 'Retainer charges ready to invoice')]),
    ('pause', 'Pause or end a retainer', '''
<p>Open the retainer and switch on <strong>Paused</strong> to stop new charges without losing the setup. Set an end date to stop it on a date, or tap the trash icon to delete it. Charges already created stay.</p>
<p>If your workspace goes back to Free, retainers pause until you upgrade again. Existing budgets stay in place but can't be changed.</p>''', []),
    ]))

# ---------------------------------------------------------------- Free vs Pro
PAGES.append(dict(
    slug='free-vs-pro', title='Free vs Pro', nav='Free vs Pro',
    desc='What Cruxy Free and Cruxy Pro include, what happens at the limits, and what happens if Pro ends.',
    intro='Free covers time tracking and invoicing for up to 2 active clients. Pro is $4.99 a month for everything else.',
    sections=[
    ('compare', 'What each plan includes', '''
<div class="tbl-wrap"><table class="cmp">
<thead><tr><th></th><th>Free</th><th>Pro<br><span>$4.99/mo</span></th></tr></thead>
<tbody>
<tr><td>Time tracking</td><td>&#10003;</td><td>&#10003;</td></tr>
<tr><td>Professional invoices: create, share and download</td><td>&#10003;</td><td>&#10003;</td></tr>
<tr><td>Reminders to log your time</td><td>&#10003;</td><td>&#10003;</td></tr>
<tr><td>Overdue invoice alerts</td><td>&#10003;</td><td>&#10003;</td></tr>
<tr><td>Active clients</td><td>2</td><td>Unlimited</td></tr>
<tr><td>Emailed invoices</td><td>3 a month</td><td>Unlimited</td></tr>
<tr><td>Automatic payment reminders to your clients</td><td></td><td>&#10003;</td></tr>
<tr><td>Project budgets and tracking</td><td></td><td>&#10003;</td></tr>
<tr><td>Monthly budget rollover</td><td></td><td>&#10003;</td></tr>
<tr><td>Retainers for recurring fixed fees</td><td></td><td>&#10003;</td></tr>
<tr><td>Invoices without the Cruxy footer</td><td></td><td>&#10003;</td></tr>
</tbody></table></div>
<p>Free also includes unlimited projects and tasks, CSV import from Clockify, Toggl and Harvest, and CSV export. Free is not a trial. It doesn't expire.</p>''', []),
    ('clients-limit', 'What counts as an active client', '''
<p>Free includes 2 active clients. A client you've archived doesn't count, and keeps all its history, read-only. When you finish with a client, archive them to make room.</p>
<p>If you try to add a third active client on Free, Cruxy offers Pro instead.</p>''', []),
    ('email-limit', 'The emailed invoice limit', '''
<p>Free includes 3 emailed invoices or reminders a month, renewing on the 1st (in your time zone). The email sheet shows how many you have left. <strong>Sharing and downloading invoices stay free and unlimited</strong>, so you can always send a PDF yourself.</p>''',
     [shot(None, 'The email limit message', 'The Upgrade to Pro sheet shown when the free monthly emails are used up')]),
    ('upgrade', 'Upgrade to Pro', '''
<p>Tap <strong>Upgrade</strong> when Cruxy offers it, or open <strong>Settings &gt; Profile</strong> and tap <strong>Upgrade to Pro</strong>. See <a href="../billing/">Billing</a> for how payment and cancelling work.</p>''', []),
    ('pro-ends', 'If Pro ends', '''
<p>Your data stays. When Pro ends:</p>
<ul>
<li>If you have more than 2 active clients, Cruxy asks you to choose 2 to keep active. The rest are archived, read-only.</li>
<li>Emailing invoices is limited to 3 a month. Sharing and downloading are still free.</li>
<li>Budgets keep what's set but can't be changed. Retainers pause.</li>
<li>PDFs show the small Cruxy credit again.</li>
</ul>
<p>Upgrade again at any time and the limits lift.</p>''', []),
    ]))

# ---------------------------------------------------------------- Billing
PAGES.append(dict(
    slug='billing', title='Billing', nav='Billing',
    desc='How billing works for Cruxy Pro: upgrading, receipts, updating your card, cancelling, and refunds.',
    intro='Cruxy Pro is $4.99 a month. Payments are handled by Stripe.',
    sections=[
    ('upgrade', 'Upgrade to Pro', '''
<ol>
<li>Open <strong>Settings &gt; Profile</strong> and tap <strong>Upgrade to Pro</strong>. You can also tap <strong>Upgrade</strong> when Cruxy offers it, for example when you reach a limit.</li>
<li>Enter your payment details on the Stripe checkout page.</li>
<li>When you return to Cruxy, you're on Pro straight away.</li>
</ol>
<p>Pro is billed monthly. There's no contract.</p>''',
     [shot(None, 'The Upgrade to Pro sheet', 'The Upgrade to Pro sheet with the $4.99/mo button')]),
    ('receipts', 'Receipts and invoices', '''
<p>Stripe handles your payments and billing history. You can see past payments, and download receipts, from the billing page described below. If you need a receipt in a particular form, email <a href="mailto:support@cruxy.io">support@cruxy.io</a>.</p>''', []),
    ('manage', 'Manage your subscription or update your card', '''
<p>Open <strong>Settings &gt; Profile</strong> and tap <strong>Manage Subscription</strong>. This opens Stripe's billing page, where you can update your card, see your payments, or cancel.</p>''',
     [shot(S+'settings-profile.png', 'The Profile tab in Settings with the Plan row')]),
    ('cancel', 'Cancel Pro', '''
<p>Open <strong>Settings &gt; Profile</strong>, tap <strong>Manage Subscription</strong>, and cancel there. You can cancel at any time. In the last week of your plan Cruxy shows a banner with the date it ends and a <strong>Keep Pro</strong> button if you change your mind. After that your workspace moves to Free. See <a href="../free-vs-pro/#pro-ends">If Pro ends</a>.</p>''', []),
    ('refunds', 'Refunds', '''
<p>Fees are non-refundable except as required by law. If you were charged by mistake, email <a href="mailto:support@cruxy.io">support@cruxy.io</a> and we'll look into it.</p>
<p>Deleting your account cancels Pro straight away and doesn't refund the current period.</p>''', []),
    ]))

# ---------------------------------------------------------------- Account
PAGES.append(dict(
    slug='account', title='Account', nav='Account',
    desc='Manage your Cruxy account: profile, workspace name, week start, Google sign-in, installing on your phone, logging out and deleting your account.',
    intro='Your profile, how you sign in, and how to leave.',
    sections=[
    ('profile', 'Edit your profile', '''
<p>Tap your avatar, then the gear icon, and open the <strong>Profile</strong> tab. You can change your name, avatar color and workspace name, and choose which day the week starts on (Sunday or Monday). The week start is saved on each device, so set it on every device you use. Tap <strong>Save</strong>.</p>''',
     [shot(S+'settings-profile.png', 'The Profile tab in Settings')]),
    ('google', 'Sign in with Google', '''
<p>Sign-up is by email and password. To add Google sign-in afterward, open <strong>Settings &gt; Profile</strong> and tap <strong>Connect Google</strong>. From then on you can tap <strong>Continue with Google</strong> on the sign-in screen.</p>
<p>Continue with Google only works for an account you've already created. If you try it without one, Cruxy asks you to sign up with your email first.</p>''', []),
    ('password', 'Reset your password', '''
<p>On the sign-in screen, tap <strong>Forgot Password?</strong>, enter your email and tap <strong>Send Reset Link</strong>. Open the email, tap the link and choose a new password. For privacy we show the same message whether or not an account exists for that email.</p>''', []),
    ('install', 'Install Cruxy on your phone', '''
<p>Cruxy works in your browser at get.cruxy.io. To open it like an app:</p>
<ul>
<li><strong>iPhone:</strong> open get.cruxy.io in Safari, tap the Share button, then <strong>Add to Home Screen</strong>.</li>
<li><strong>Android:</strong> open get.cruxy.io in Chrome, tap the menu, then <strong>Add to Home screen</strong> or <strong>Install app</strong>.</li>
</ul>
<p>Cruxy updates itself. If it reloads after an update, that's why.</p>''',
     [shot(None, 'Adding Cruxy to the home screen on iPhone', 'The Safari Share sheet with Add to Home Screen highlighted')]),
    ('logout', 'Log out', '''
<p>Tap your avatar in the top right and choose <strong>Log Out</strong>.</p>''', []),
    ('delete', 'Delete your account', '''
<p>Open <strong>Settings &gt; Profile</strong>, tap <strong>Delete Account</strong>, type <strong>DELETE</strong> and confirm.</p>
<ul>
<li>Your workspace and everything in it is permanently deleted: clients, time entries, invoices and settings.</li>
<li>A Pro subscription is cancelled straight away, with no refund for the current period.</li>
<li>There is no undo and no grace period.</li>
</ul>
<p>Export what you need first. See <a href="../time/#export">Export your time</a>, and download your invoice PDFs. If you can't sign in, email <a href="mailto:support@cruxy.io">support@cruxy.io</a> from the address on your account.</p>''',
     [shot(None, 'The Delete account sheet', 'The Delete account sheet with the DELETE confirmation box')]),
    ]))

# ---------------------------------------------------------------- Troubleshooting
PAGES.append(dict(
    slug='troubleshooting', title='Troubleshooting', nav='Troubleshooting',
    desc='Fixes for common Cruxy problems: invoice emails that did not arrive, free email limit, cannot create an invoice, sync problems and sign-in issues.',
    intro='Quick answers to the problems people run into most.',
    sections=[
    ('email-missing', 'An invoice email didn\'t arrive', '''
<p>Ask your client to check their spam or junk folder first. Then:</p>
<ul>
<li>Check the billing email in the client's details for typos.</li>
<li>On an unpaid invoice, a note under the title tells you if a reminder bounced or was marked as spam.</li>
<li>If it still won't arrive, tap <strong>Download</strong> on the invoice and send the PDF yourself. It's free and unlimited.</li>
</ul>''', []),
    ('free-emails', 'I used up my free emails', '''
<p>Free includes 3 emailed invoices or reminders a month, and the count restarts on the 1st. You can still share or download invoices and send them yourself. Or <a href="../free-vs-pro/">go Pro</a> for unlimited.</p>''', []),
    ('cant-invoice', 'I can\'t create an invoice', '''
<p>Check these:</p>
<ul>
<li><strong>The client has no hourly rate.</strong> Set a rate above 0 in the client's details.</li>
<li><strong>There's nothing to invoice.</strong> The period may have no billable time, or it's already on another invoice.</li>
<li><strong>The period has more than one currency.</strong> Invoice each currency on its own.</li>
<li><strong>The invoice number already exists.</strong> Pick another number.</li>
</ul>''', []),
    ('currency', 'I can\'t change a client\'s currency', '''
<p>A client with unbilled time or charges can't change currency. Invoice or remove them first, then change it and update the hourly rate, since it isn't converted.</p>''', []),
    ('timer-other-device', '"Timer stopped on another device"', '''
<p>Your timer runs across your devices. If you stop it on one, the others show this message. The time is logged once, by the device that stopped it.</p>''', []),
    ('sync', "My entries aren't syncing", '''
<p>New entries are saved on your device and sent when you're online. A banner shows the status. If an entry can't be saved, for example its client or project was deleted, the banner offers <strong>Retry</strong> or <strong>Discard</strong>. Discarding removes it from your device for good.</p>
<p>Editing or deleting entries needs a connection. Check you're online and try again.</p>''', []),
    ('signin', "I can't sign in", '''
<ul>
<li>Use <strong>Forgot Password?</strong> to reset your password.</li>
<li>If you tried <strong>Continue with Google</strong> and were told there's no account, sign up with your email first, then connect Google in Settings.</li>
<li>After signing up, you may need to confirm your email before you can sign in.</li>
</ul>
<p>Still stuck? Email <a href="mailto:support@cruxy.io">support@cruxy.io</a> from the address on your account.</p>''', []),
    ('reloaded', 'The app reloaded by itself', '''
<p>When we release an update, Cruxy refreshes itself the next time it checks. If you were typing in a form, finish and save before you step away.</p>''', []),
    ]))

# ---------------------------------------------------------------- Contact
PAGES.append(dict(
    slug='contact', title='Contact us', nav='Contact us',
    desc='Contact Cruxy support by email, and what to include so we can help quickly.',
    intro='Email us and a real person will reply.',
    sections=[
    ('email', 'Email support', '''
<p>Write to <a href="mailto:support@cruxy.io">support@cruxy.io</a>. We reply as soon as we can.</p>
<p>It helps if you include:</p>
<ul>
<li>The email address on your Cruxy account</li>
<li>What you were trying to do, and what happened instead</li>
<li>A screenshot, if you can</li>
<li>Whether you were using a phone or a computer, and which browser</li>
</ul>
<p>Please don't send passwords or card numbers.</p>''', []),
    ('billing-privacy', 'Billing, privacy and account requests', '''
<p>For billing questions, privacy requests, or help deleting your account, email the same address from the email on your account. See <a href="../billing/">Billing</a> and <a href="../account/#delete">Delete your account</a>.</p>''', []),
    ('feedback', 'Ideas and feedback', '''
<p>Missing something? Tell us. We read every message.</p>''', []),
    ]))

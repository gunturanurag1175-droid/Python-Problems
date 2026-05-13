"""Ask the user to enter a filename. Check if it starts with "report_" and ends with ".pdf".
Print an appropriate message for each check."""

filename = input("Enter file name: ")
if filename.startswith("report_"):
    print("✓ Starts with 'report_'")
else:
    print("✗ Does not start with 'report_'")
if filename.endswith(".pdf"):
    print("✓ Is a PDF file")
else:
    print("✗ Not a PDF file")
# Interactive Expense Tracking Dashboard using Power BI

## Project Overview

The goal of this project was to develop an interactive Power BI dashboard for real-time expense tracking, providing users with an effortless way to monitor their expenses and enhance their financial awareness and decision-making.

## Features

- Real-time Data: The dashboard fetches and updates expense data in real-time, ensuring that users always have up-to-date information.

- User-Friendly Interface: The dashboard offers an intuitive and user-friendly interface, making it easy for users to interact with and navigate through their expense data.

- Dynamic Visualizations: Through dynamic visualizations such as charts and graphs, users can gain insights into their spending patterns, categories, and trends over time.

## Code Snippets

### Real-Time Data Fetching

```dax
// DAX query to fetch real-time expense data from the database
Expenses = 
VAR CurrentUser = USERNAME()
RETURN
    FILTER(ExpenseTable, ExpenseTable[User] = CurrentUser)

```
## Future Enhancements
* Integration with External APIs: Incorporate APIs to fetch data from financial institutions or third-party expense tracking tools, enabling automatic expense updates.

* Customized Alerts: Implement customizable alerts for users to receive notifications based on expense thresholds or unusual spending patterns.

## Conclusion
The interactive Power BI dashboard successfully provides users with a seamless and real-time expense tracking experience. By visualizing their expenses, users can make informed financial decisions and improve their overall financial awareness.

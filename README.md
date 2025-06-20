# CST8919 Lab 2: Web App Threat Detection using Azure Monitor and KQL

## 🧠 What I Learned

During this lab, I learned how to deploy a Python Flask web application to Azure App Service and integrate it with Azure Monitor to detect analyze the application logs. I explored how to collect and analyze diagnostic logs using Kusto Query Language (KQL), and how to create real-time alert rules that can notify administrators of potential brute-force login attempts.

## ⚠️ Challenges Faced

- **KQL Debugging**: Writing an accurate KQL query to distinguish failed login attempts from other requests took some iteration, particularly in filtering the correct log categories and fields.
- **Alert Configuration**: Tuning the alert rule to align with the required testing the frequency and threshold settings.

## 💡 Improvement Suggestions for Real-World Detection

In a production environment, I would:
- Enhance logging with more context, such as user agent, IP address, and geolocation.
- Track the number of failed attempts per IP or user within a timeframe to improve brute-force detection.

---

## 🔎 KQL Query & Explanation

```kql
AppServiceConsoleLogs
| where Level == "Informational"
| where ResultDescription has "Failed login attempt"
| where TimeGenerated > ago(5min)
| project TimeGenerated, Level, ResultDescription
```

### Explanation:
- `AppServiceConsoleLogs`: This is the log table that captures console outputs (e.g., `print()` or `logging.info()`) from the Flask application running on Azure App Service.
- `where Level == "Informational"`: Filters logs to include only informational-level entries, which are typically non-critical but useful messages logged by the app.
- `where ResultDescription has "Failed login attempt"`: Narrows down the logs to only those that indicate a failed login event, assuming this is the exact message used in your app's log.
- `where TimeGenerated > ago(5min)`: Restricts the results to entries from the past 5 minutes to support real-time detection use cases.
- `project TimeGenerated, Level, ResultDescription`: Selects and displays only the relevant columns for analysis and alerting.

---

## 🎥 Demo Video

[🔗 Watch the 5-minute demo on YouTube](https://youtu.be/2RTAGdUW4Jw)


# MailSquad
**Email automation using LangGraph, LangChain, and ToolUse**

## 🚀 Overview
MailSquad is a smart email automation tool that processes incoming emails, categorizes them, researches relevant information, and drafts professional replies — all powered by LangGraph, LangChain, and ToolUse.

## 📨 Reply to a Customer Email

1. **Receive the email**
2. **Categorize** the email as one of the following:
   - Sales
   - Custom Enquiry
   - Off-topic
   - Customer Complaint
3. **Generate keywords** using the category and initial email for research
4. **Draft a reply**
5. **Analyze** the draft reply
6. **Rewrite** if necessary

---

## 🧠 LangGraph Pipeline

### Define:
- **State**
- **Nodes**
- **Conditional Edges**

---

### 🧩 Nodes

1. `categorize_email` - Classifies the email into a predefined category.
2. `research_info_search` - Searches for relevant information based on the category and email content.
3. `draft_email_writer` - Drafts a reply using the email content and research info.
4. `analyze_draft_email` - Evaluates the quality and relevance of the draft.
5. `rewrite_email` - Improves the draft if needed.
6. `no_rewrite` - Skips rewriting if the draft is acceptable.
7. `state_printer` - (Optional) Logs the state at any point in the workflow.

---

## 🛠️ Build the Graph

1. **Add Nodes**
2. **Add Edges**
3. **Compile Workflow**
4. ✅ Boom! Ready to invoke!

---

## 🧪 Example Use Case
Incoming customer queries get automatically processed, categorized, researched, and responded to — saving hours of manual work and ensuring consistency in tone and accuracy.

---

## 📦 Tech Stack
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [LangChain](https://www.langchain.com/)
- [ToolUse](https://app.tavily.com/)

---

> Automate replies. Accelerate engagement.

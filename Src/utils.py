def format_web_summary(question, web_output):
    return f"""
## Answer: {question}
The following summary is based on recent and reliable sources.
{web_output}
---
*This response was generated using real-time web search data.*
"""

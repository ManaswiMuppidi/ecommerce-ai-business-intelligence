def build_prompt(metrics):
    return f"""You are an e-commerce business analyst.
Use only these validated metrics: {metrics}.
Return: 3 observations, 3 business actions, 2 data limitations,
and 3 management follow-up questions. Do not invent facts."""

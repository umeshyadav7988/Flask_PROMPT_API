def get_prompt(situation, level, file_type):
    match_criteria = {
        ("Commercial Auto", "Structure", "Summary Report"): "Prompt 1",
        ("General Liability", "Summarize", "Deposition"): "Prompt 2",
        ("Commercial Auto", "Summarize", "Summons"): "Prompt 3",
        ("Workers Compensation", "Structure", "Medical Records"): "Prompt 4",
        ("Workers Compensation", "Summarize", "Summons"): "Prompt 5",
    }

    key = (situation.strip(), level.strip(), file_type.strip())
    
    if key in match_criteria:
        return match_criteria[key]
    else:
        raise ValueError("Invalid Prompt")

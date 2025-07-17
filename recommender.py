def generate_recommendations(age, bmi, bp, glucose):
    tips = []
    if bmi > 30:
        tips.append("Consider a weight loss plan to reduce BMI.")
    if bp > 130:
        tips.append("Monitor blood pressure regularly; reduce salt intake.")
    if glucose > 140:
        tips.append("Limit sugar intake and consider a diabetes screening.")
    if age > 50:
        tips.append("Annual checkups are recommended after age 50.")
    if not tips:
        tips.append("Maintain current healthy lifestyle!")
    return tips

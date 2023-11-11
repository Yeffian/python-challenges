import random

def reports(student_no):
    economics_teacher_comments = [
        "Your understanding of supply and demand is evident in your analysis. Great job!",
        "Consider providing more real-world examples to strengthen your argument.",
        "You've demonstrated a solid grasp of economic theories. Keep up the good work!",
        "Be sure to cite your sources when referencing economic data or research findings.",
        "Your explanation of macroeconomic concepts is clear and concise. Well done!",
        "Incorporate more economic terminology to enhance the academic rigor of your analysis.",
        "Your discussion on market structures is insightful, but remember to address potential counterarguments.",
        "Excellent use of economic models to support your analysis. Impressive!",
        "Consider exploring the historical context of economic events to provide a comprehensive analysis.",
        "Make sure to proofread your work for grammatical errors and clarity of expression.",
        "Your application of economic principles to real-world scenarios is commendable.",
        "Consider discussing the policy implications of the economic phenomena you analyze.",
        "Your understanding of international trade concepts is evident in your thoughtful analysis.",
        "Support your arguments with statistical evidence to strengthen the empirical basis of your analysis.",
        "Consider exploring the ethical dimensions of economic decisions in your discussion.",
        "Well-organized and structured analysis. It's evident that you put thought into your presentation.",
        "Remember to consider alternative perspectives when evaluating economic policies or strategies.",
        "Your use of visual aids, such as graphs and charts, enhances the clarity of your presentation.",
        "Great effort in integrating current economic events into your analysis. Stay informed!",
        "Consider elaborating on the long-term implications of the economic trends you identify.",
        "Your engagement with economic literature is evident in your well-referenced paper. Keep it up!",
    ]

    result = []

    for i in range(student_no):
        result.append(random.choice(economics_teacher_comments))
    
    return result

for report in reports(5):
    print(report)
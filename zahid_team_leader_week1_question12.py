#Question no 12

for i in range(1,5):
    seconde_term = float(input(f"Enter midterm grade Subject {i}:"))
    final_term = float(input(f"Enter final term grade {i}:"))
    average_marks_subject = (seconde_term * 0.4) + (final_term * 0.6)
    if average_marks_subject >= 50:
        final_result = "SUCCESSFUL"
    else:
        final_result = "FAILED"
    print(f"Averege Marks{average_marks_subject:.2f} Result {final_result}")

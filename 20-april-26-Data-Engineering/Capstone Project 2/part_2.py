import json
import csv

def read_students_txt(filename):
    with open(filename,'r') as f:
        return [line.strip() for line in f if line.strip()]

def load_marks_json(filename):
    with open(filename,'r') as f:
        data=json.load(f)
        return data['students']

def load_attendance_csv(filename):
    attendance_list=[]
    with open(filename,mode='r') as f:
        reader=csv.DictReader(f)
        for row in reader:
            attendance_list.append({
                "name": row['name'],
                "days_present": int(row['days_present']),
                "total_days": int(row['total_days'])
            })
    return attendance_list

def calculate_avg_marks(marks_list):
    return sum(marks_list)/len(marks_list) if marks_list else 0

def get_attendance_pct(present, total):
    return (present/total)*100

def get_grade(mark):
    if mark>=90: return "A"
    elif mark>=75: return "B"
    elif mark>=50: return "C"
    else: return "Fail"

# PART 1
names=read_students_txt('students.txt')
print(f"Names = {names}")
print(f"Total entries: {len(names)}") 

unique_names=list(set(names)) 
print(f"Unique names: {unique_names}")

name_counts={name:names.count(name) for name in set(names)}
print(f"Name counts: {name_counts}")

with open('unique_students.txt','w') as f: 
    for name in sorted(unique_names):
        f.write(name+"\n")

# PART 2
marks_data=load_marks_json('marks.json')
print("\nStudent Marks:")
for s in marks_data:
    print(f"{s['name']}: {s['marks']}")

topper=max(marks_data, key=lambda x: x['marks'])
lowest=min(marks_data, key=lambda x: x['marks'])
print(f"Highest: {topper['name']} ({topper['marks']})")
print(f"Lowest: {lowest['name']} ({lowest['marks']})")

all_marks=[s['marks'] for s in marks_data]
avg_marks=calculate_avg_marks(all_marks)
print(f"Average Marks: {avg_marks:.2f}")

print("\nPython Course Students:")
python_students=[s['name'] for s in marks_data if s['course'] == 'Python']
print(python_students)

course_counts={}
for s in marks_data:
    course_counts[s['course']]=course_counts.get(s['course'],0)+1
print(f"Course distribution: {course_counts}")

# PART 3
attendance_data=load_attendance_csv('attendance.csv') 
print("\nAttendance Details:")
best_att_val=-1
best_att_student= ""

attendance_results={}
for row in attendance_data:
    pct=get_attendance_pct(row['days_present'],row['total_days'])
    attendance_results[row['name']]=pct
    print(f"{row['name']}: {pct}%") 
    
    if pct<80: 
        print(f"  -- ALERT: {row['name']} attendance below 80%!")
    
    if pct>best_att_val:
        best_att_val=pct
        best_att_student=row['name']
print(f"Best Attendance: {best_att_student}")

# PART 4
print(f"\nMarks List Stats: High: {max(all_marks)}, Low: {min(all_marks)}, Sum: {sum(all_marks)}")
all_courses=tuple(s['course'] for s in marks_data) 
print(f"Courses Tuple: {all_courses}")
unique_courses=set(all_courses) 
print(f"Unique Courses Set: {unique_courses}")

marks_dict={s['name']: s['marks'] for s in marks_data} 

# PART 5
print("\nPass/Fail Status:")
for name, mark in marks_dict.items():
    status="Pass" if mark >= 50 else "Fail"
    print(f"{name}: {status}")

print("\nHigh Performers (Marks > 80 & Att > 85%):")
for s in marks_data:
    name=s['name']
    if s['marks'] > 80 and attendance_results.get(name, 0) > 85:
        print(name)

# PART 7
final_data={}
for s in marks_data:
    name=s['name']
    final_data[name]={
        "marks": s['marks'],
        "attendance": attendance_results.get(name, 0),
        "course": s['course'],
        "grade": get_grade(s['marks'])
    }

print("\nCombined Summary:")
for name, info in final_data.items():
    print(f"Name: {name} | Marks: {info['marks']} | Att: {info['attendance']}% | Course: {info['course']} | Grade: {info['grade']}")

eligible=[] 
needs_imp=[]
for name, info in final_data.items():
    if info['marks']>=75 and info['attendance']>=80:
        eligible.append(name)
    else:
        needs_imp.append(name)

# PART 8
with open('report.txt','w') as f:
    f.write("Student Report\n")
    for name, info in final_data.items():
        f.write(f"{name} - Marks: {info['marks']} - Attendance: {info['attendance']}% - Grade: {info['grade']}\n")

with open('eligible_students.txt', 'w') as f: 
    for name in eligible:
        f.write(name + "\n")

print("\n" + "="*30)
print("FINAL SUMMARY REPORT")
print("="*30)
print(f"Topper: {topper['name']}")
print(f"Best Attendance: {best_att_student}")
print(f"Average Marks: {avg_marks:.1f}")
print(f"Eligible Students: {', '.join(eligible)}")
print(f"Students Needing Improvement: {', '.join(needs_imp)}")
# Evaluate-teacher-performance
This program evaluates teachers' performance based on their students' rank among the entire high school.


## Background
There are currently 414 students in grade 10 at Longchi high school. Chinese, Math, and English are mandatory, while students have the freedom to choose any 3 from the 6 selective courses, that is, Physics, Chemistry, Biology, Geology, Politics and History. Students are divided into 8 class units (class 801 - class 808) based on their choice of courses. Theorectically, there should be 20 classes (6!/3! different combinations). However, the administrative stuff manage to form just 8 class units based on popular combinations. For instance, selection of Phyisic, Chemistry and Biology is a common track for students who are passionate about science. Each course of each class unit is taught by a different teacher. Chinese for Class 801 is covered by Mr Cao but Chinese for class 802 is covered by Ms Chen.

This school focuses mainly on students grades just like every other Chinese high school does. To evaluate teachers performances, the principle ranks students not only by total grades but also by every single course. Attached is a sample for a recent final exam result. 
![](https://github.com/rushuifang/Evaluate-teacher-performance/blob/master/dataSnapshot.png)

The dataset contains empty elements because selectives are inevitably not chosen by every students. It's important to inverstigate the dataset before processing it.

## Goal
For each course, every top 6% students earn their class unit/ correponding teacher 0.95 points, the rest of 94% is divided into 20 intervals. Students would earn 0.9, 0.85, ..., 0.05, 0.03 and 0.02 points accordingly for those 20 intervals. Teacher who is in charge of that specific course in that class unit with the highest points gets cash prize.

## Note
* Total number of students in each course is different.
* Rank can be duplicate if multiple students have the same grade.
* Total number of students attending monthly exams varies.
* Results should be represented in excel format and attached to the same finals.xlsx file.

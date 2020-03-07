# Evaluate-teacher-performance
This program evaluates teachers' performance based on their students' rank among the entire high school.

Background:
There are currently 414 students in grade 10 at Longchi high school. Chinese, Math, and English are mandatory for all the students, while they have the freedom to choose any 3 from the 6 selective courses (Physics, Chemistry, Biology, Geology, Politics and History). Students are divided into 8 class units (class 801 - class 808) based on their choice of courses. Theorectically, there should be 20 classes (6!/3! different combinations). However, this Chinese high school manages to form 8 class units based on some structured combinations, for example, selection of Phyisic, Chemistry and Biology is a common track for students who are passionate about science. Each class unit is taught by a different teacher. (Chinese for Class 801 is covered by Mr Cao but Chinese for class 802 is covered by Ms Chen.)

Goal:
This school focus on students grades like every other Chinese high school does. To stimulate teachers performances, the principle ranks students not only by total grades but also by every single subject. Attached is a sample for the recent final exam. 
![](https://github.com/rushuifang/Evaluate-teacher-performance/blob/master/dataSnapshot.png)
The dataset contains empty elements because selectives are not chosen by every students. Therefore, they are not in the rank for competion of that subject.

For each subjects, every top 6% students earn their class 0.95 point, the rest of them is divided into 20 intervals. Students earn their class 0.9,0.85,..., 0.05, then 0.03 and 0.02 in those 20 intervals. Teacher who is in charge of the class units of that specific subject with the highest points can get cash prize.

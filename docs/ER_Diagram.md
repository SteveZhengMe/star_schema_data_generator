# ER Diagram

``` mermaid
erDiagram
    professor_info_dim ||--o{ curriculum_fact: professor_ID
    student_info_dim ||--o{ curriculum_fact: student_ID
    course_info_dim ||--o{ curriculum_fact: course_ID
    date_info_dim ||--o{ curriculum_fact: date_ID

    student_info_dim ||--o{ drop_off_Fact: student_ID
    date_info_dim ||--o{ drop_off_Fact: drop_off_date_ID
    drop_off_reason_dim ||--o{ drop_off_Fact: reason

    professor_info_dim {
        id int
        name str
        gender str
        dob date
        onboarding_date date
    }

    student_info_dim {
        id int
        name str
        gender str
        dob date
        ori_continent str
        program str
        register_date date
        enroll_date date
    }

    course_info_dim {
        id int
        name str
        program str
        course_duration_year int
    }

    date_info_dim {
        id int
        theDate date
        term_name str
        year int
        month int
        day int
        week_num int
    }

    drop_off_reason_dim {
        id int
        caused_by_remote int
        reason str
    }

    drop_off_Fact {
        id int
        student_ID int
        drop_off_date_ID int
        drop_off_reason_id int 
    }

    curriculum_fact {
        id int
        student_ID int
        course_ID int
        professor_ID int
        start_date_ID date
        end_date_ID date
        participate_score float
        lab_score float
        theory_score float
        final_score float
        online_days int
        classroom_days int
    }
```

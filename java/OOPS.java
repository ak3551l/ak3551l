class Student{
    String name;
    static String school;

    public static void changeSchool() {
        school = "newschool";
    }
}

public class OOPS {
    public static void main(String[] args) {
        Student.school = "ABC";
        Student student1 = new Student();
        student1.name = "Tony";
        System.out.println(Student.school);
    }
}

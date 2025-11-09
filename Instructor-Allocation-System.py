class Instructor:
    def __init__(self):
        self.__name = None
        self.__technology_skill = []
        self.__experience = 0
        self.__avg_feedback = 0.0

    def set_name(self, name):
        self.__name = name

    def set_technology_skill(self, skills):
        if isinstance(skills, list):
            self.__technology_skill = skills
        else:
            self.__technology_skill = [skills]

    def set_experience(self, exp):
        self.__experience = exp

    def set_avg_feedback(self, feedback):
        self.__avg_feedback = feedback

    def get_name(self):
        return self.__name

    def get_technology_skill(self):
        return self.__technology_skill

    def get_experience(self):
        return self.__experience

    def get_avg_feedback(self):
        return self.__avg_feedback
    
    def check_eligibility(self):
        if self.__experience > 3 and self.__avg_feedback >= 4.5:
            return True
        elif self.__experience <= 3 and self.__avg_feedback >= 4.0:
            return True
        else:
            return False

    def allocate_course(self, technology):
        if self.check_eligibility() and technology in self.__technology_skill:
            return True
        else:
            return False

    def display_details(self):
        print(f"Instructor Name: {self.__name}")
        print(f"Skills: {', '.join(self.__technology_skill)}")
        print(f"Experience: {self.__experience} years")
        print(f"Average Feedback: {self.__avg_feedback}")

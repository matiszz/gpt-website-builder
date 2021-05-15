from OpenAIController import OpenAIController

sample_description = "Velox is a real-time platform that helps remote teams keeping organized chats. In Velox, " \
                     "you can create new conversations for different topics. "

sample_testimonial_names = ["Martha Taylor", "Lucy Williams", "John Smith", "Kevin Brown"]
sample_testimonial_roles = ["Senior Product Designer", "UI Develeoper", "CEO", "CIO", "DESIGNER"]


if __name__ == '__main__':
    # execute only if run as the entry point into the program

    openAI = OpenAIController()
    #openAI.get_tagline(sample_description)

    #openAI.get_sample_testimonial_bio(sample_description)
    print("---")
    #openAI.get_sample_testimonial_name(sample_testimonial_names)
    print("---")
    #openAI.get_sample_testimonial_role(sample_testimonial_roles)


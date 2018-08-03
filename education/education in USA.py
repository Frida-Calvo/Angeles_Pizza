import matplotlib.pyplot as plt

import education
a_state_record = education.get_state("california")

list_of_state_record = education.get_all_states()


science = []
studentAttend = []
funding = []

for info in list_of_state_record:
    science.append(info["data"]["score"]["science"][0]["scale score"])
    studentAttend.append(info["data"]["attendance"]["average student rate"])
    funding.append(info["data"]["funding"]["revenue"])

print(len(science))
print(len(funding))

##science.sort()
plt.plot(funding, science, 'ro')
plt.xlabel("Funding")
plt.ylabel("Score in Science")
plt.title("Students from K-12's Science Scores compared to School Funding")

##plt.axis([70,100,1*1e10,6*1e10])
plt.show()
    

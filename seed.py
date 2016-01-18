import random

names = [ "Nicola", "Karen", "Fiona", "Susan", "Claire", "Sharon", "Angela", "Gillian", "Julie", "Michelle", "Jacqueline", "Amanda", "Tracy", "Louise", "Jennifer", "Alison", "Sarah", "Donna", "Caroline", "Elaine", "Lynn", "Margaret", "Elizabeth", "Lesley", "Deborah", "Pauline", "Lorraine", "Laura", "Lisa", "Tracey", "Carol", "Linda", "Lorna", "Catherine", "Wendy", "Lynne", "Yvonne", "Pamela", "Kirsty", "Jane", "Emma", "Joanne", "Heather", "Suzanne", "Anne", "Diane", "Helen", "Victoria", "Dawn", "Mary", "Samantha", "Marie", "Kerry", "Ann", "Hazel", "Christine", "Gail", "Andrea", "Clare", "Sandra", "Shona", "Kathleen", "Paula", "Shirley", "Denise", "Melanie", "Patricia", "Audrey", "Ruth", "Jill", "Lee", "Leigh", "Catriona", "Rachel", "Morag", "Kirsten", "Kirsteen", "Katrina", "Joanna", "Lynsey", "Cheryl", "Debbie", "Maureen", "Janet", "Aileen", "Arlene", "Zoe", "Lindsay", "Stephanie", "Judith", "Mandy", "Jillian", "Mhairi", "Barbara", "Carolyn", "Gayle", "Maria", "Valerie", "Christina", "Marion" ] 

dens = [ "Tiger", "Wolf", "Bear", "Webelos 1", "Webelos 2" ] 

mixed = RND.randomList(names)

for name in mixed:
	age = random.randint(5,10)
	dennumb = random.randint(1,5)

	DB.SQL("INSERT INTO racers (racer_id, racer_name, racer_age, racer_den) values (NULL,\"" + str(name) + "\", " + str(age) + ", \"" + str(dennumb) + "\");")

for den in dens:
	DB.SQL("INSERT INTO dens (id, name) values (NULL,\"" + str(den) + "\");")

DB.commit()


gfile = "D:\\user1\\Downloads\\glove.840B.300d\\glove.840B.300d.txt"
import numpy as np
import pickle

#load the dataset
print ("Loading Glove Model")
    
with open(gfile, encoding="utf8" ) as f:
    content = f.readlines()
model = {}
    
ind = 0
    
for line in content:
    try:
        splitLine = line.split()
        word = splitLine[0]
        embedding = np.array([float(val) for val in splitLine[1:]])
        model[word] = embedding
    except ValueError:
        print(splitLine[0])

print ("Done.",len(model)," words loaded!")

#extract experiment items from model
#weat 1
flowers = ['aster', 'clover', 'hyacinth', 'marigold', 'poppy', 'azalea', 'crocus', 'iris', 'orchid', 'rose', 'bluebell', 'daffodil', 'lilac', 'pansy', 'tulip', 'buttercup', 'daisy', 'lily', 'peony', 'violet', 'carnation', 'gladiola',
'magnolia', 'petunia', 'zinnia']
insects = ['ant', 'caterpillar', 'flea', 'locust', 'spider', 'bedbug', 'centipede', 'fly', 'maggot', 'tarantula',
'bee', 'cockroach', 'gnat', 'mosquito', 'termite', 'beetle', 'cricket', 'hornet', 'moth', 'wasp', 'blackfly',
'dragonfly', 'horsefly', 'roach', 'weevil']
pleasant = ['caress', 'freedom', 'health', 'love', 'peace', 'cheer', 'friend', 'heaven', 'loyal', 'pleasure', 'diamond', 'gentle', 'honest', 'lucky', 'rainbow', 'diploma', 'gift', 'honor', 'miracle', 'sunrise', 'family',
'happy', 'laughter', 'paradise', 'vacation']
unpleasant = ['abuse', 'crash', 'filth', 'murder', 'sickness', 'accident', 'death', 'grief', 'poison', 'stink',
'assault', 'disaster', 'hatred', 'pollute', 'tragedy', 'divorce', 'jail', 'poverty', 'ugly', 'cancer', 'kill', 'rotten',
'vomit', 'agony', 'prison']

#weat 2
instruments = ['bagpipe', 'cello', 'guitar', 'lute', 'trombone', 'banjo', 'clarinet', 'harmonica', 'mandolin',
'trumpet', 'bassoon', 'drum', 'harp', 'oboe', 'tuba', 'bell', 'fiddle', 'harpsichord', 'piano', 'viola', 'bongo',
'flute', 'horn', 'saxophone', 'violin']
weapons = ['arrow', 'club', 'gun', 'missile', 'spear', 'axe', 'dagger', 'harpoon', 'pistol', 'sword', 'blade',
'dynamite', 'hatchet', 'rifle', 'tank', 'bomb', 'firearm', 'knife', 'shotgun', 'teargas', 'cannon', 'grenade',
'mace', 'slingshot', 'whip']
pleasant, unpleasant

#weat 3
european_3 = ['Adam', 'Harry', 'Josh', 'Roger', 'Alan', 'Frank', 'Justin',
'Ryan', 'Andrew',  'Jack', 'Matthew', 'Stephen', 'Brad', 'Greg' , 'Paul', 
'Jonathan', 'Peter',  'Amanda', 'Courtney', 'Heather', 'Melanie', 'Katie','Betsy', 'Kristin', 'Nancy', 'Stephanie', 
'Ellen', 'Lauren', 'Colleen', 'Emily', 'Megan', 'Rachel']
african_3 = [ 'Alonzo', 'Jamel',  'Theo', 'Alphonse', 'Jerome',
'Leroy',  'Torrance', 'Darnell', 'Lamar', 'Lionel', 'Tyree', 'Deion', 'Lamont', 'Malik',
'Terrence', 'Tyrone',  'Lavon', 'Marcellus',  'Wardell', 'Nichelle',
'Shereen',  'Ebony', 'Latisha', 'Shaniqua',  'Jasmine',
'Tanisha', 'Tia', 'Lakisha', 'Latoya', 'Yolanda', 'Malika',  'Yvette']
pleasant, unpleasant

#weat 4
european_4 = ['Brad', 'Brendan', 'Geoffrey', 'Greg', 'Brett',  'Matthew', 'Neil',
'Todd', 'Allison', 'Anne', 'Carrie', 'Emily', 'Jill', 'Laurie',  'Meredith', 'Sarah']
african_4 = ['Darnell', 'Hakim', 'Jermaine', 'Kareem', 'Jamal', 'Leroy', 'Rasheed',
 'Tyrone', 'Aisha', 'Ebony', 'Keisha', 'Kenya',  'Lakisha', 'Latoya', 'Tamika',
'Tanisha' ]
pleasant, unpleasant

#weat 5
european_4, african_4
pleasant_5 = ['joy', 'love', 'peace', 'wonderful', 'pleasure', 'friend', 'laughter', 'happy']
unpleasant_5 = ['agony', 'terrible', 'horrible', 'nasty', 'evil', 'war', 'awful', 'failure']

#weat  6
male = ['John', 'Paul', 'Mike', 'Kevin', 'Steve', 'Greg', 'Jeff', 'Bill']
female = ['Amy', 'Joan', 'Lisa', 'Sarah', 'Diana', 'Kate', 'Ann', 'Donna']
career = ['executive', 'management', 'professional', 'corporation', 'salary', 'office', 'business', 'career']
family = ['home', 'parents', 'children', 'family', 'cousins', 'marriage', 'wedding', 'relatives']

#weat 7
math = ['math', 'algebra', 'geometry', 'calculus', 'equations', 'computation', 'numbers', 'addition']
arts = ['poetry', 'art', 'dance', 'literature', 'novel', 'symphony', 'drama', 'sculpture']
male_term = ['male', 'man', 'boy', 'brother', 'he', 'him', 'his', 'son']
female_term = ['female', 'woman', 'girl', 'sister', 'she', 'her', 'hers', 'daughter']

#weat 8
science = ['science', 'technology', 'physics', 'chemistry', 'Einstein', 'NASA', 'experiment', 'astronomy']
arts_8 = ['poetry', 'art', 'Shakespeare', 'dance', 'literature', 'novel', 'symphony', 'drama']
male_term_8 = ['brother', 'father', 'uncle', 'grandfather', 'son', 'he', 'his', 'him']
female_term_8 = ['sister', 'mother', 'aunt', 'grandmother', 'daughter', 'she', 'hers', 'her']

#weat 9
mental_disease = ['sad', 'hopeless', 'gloomy', 'tearful', 'miserable', 'depressed']
physical_disease = ['sick', 'illness', 'influenza', 'disease', 'virus', 'cancer']
temporary = ['impermanent', 'unstable', 'variable', 'fleeting', 'short-term', 'brief', 'occasional' ]
permanent = [ 'stable', 'always', 'constant', 'persistent', 'chronic', 'prolonged', 'forever']

#weat 10
young_name = ['Tiffany', 'Michelle', 'Cindy', 'Kristy', 'Brad', 'Eric', 'Joey', 'Billy']
old_name = [ 'Ethel', 'Bernice', 'Gertrude', 'Agnes', 'Cecil', 'Wilbert', 'Mortimer', 'Edgar']
pleasant_5, unpleasant_5

#wefat 1
career_f1 = ['technician', 'accountant', 'supervisor', 'engineer', 'worker', 'educator', 'clerk', 'counselor', 
             'inspector', 'mechanic', 'manager', 'therapist', 'administrator', 'salesperson', 'receptionist', 
             'librarian', 'advisor', 'pharmacist', 'janitor', 'psychologist', 'physician', 'carpenter', 'nurse',
             'investigator', 'bartender', 'specialist', 'electrician', 'officer', 'pathologist', 'teacher', 
             'lawyer', 'planner', 'practitioner', 'plumber', 'instructor', 'surgeon', 'veterinarian', 'paramedic',
             'examiner', 'chemist', 'machinist', 'appraiser', 'nutritionist', 'architect', 'hairdresser', 'baker',
             'programmer', 'paralegal', 'hygienist','scientist']
male_term, female_term

#wefat 2
names = ['Kelly', 'Tracy', 'Jamie', 'Jackie', 'Jesse', 'Courtney', 'Lynn', 'Taylor', 'Leslie', 'Shannon',
'Stacey', 'Jessie', 'Shawn', 'Stacy', 'Casey', 'Bobby', 'Terry', 'Lee', 'Ashley', 'Eddie', 'Chris', 'Jody', 'Pat',
'Carey', 'Willie', 'Morgan', 'Robbie', 'Joan', 'Alexis', 'Kris', 'Frankie', 'Bobbie', 'Dale', 'Robin', 'Billie',
'Adrian', 'Kim', 'Jaime', 'Jean', 'Francis', 'Marion', 'Dana', 'Rene', 'Johnnie', 'Jordan', 'Carmen', 'Ollie',
'Dominique', 'Jimmie', 'Shelby']
male_term, female_term

list_all = flowers + insects+pleasant+unpleasant+instruments+weapons+european_3+african_3+\
european_4+african_4+pleasant_5+unpleasant_5+male+female+career+family+math+arts+\
male_term+female_term+science+arts_8+male_term_8+female_term_8+mental_disease+\
physical_disease+temporary+permanent+young_name+old_name+career_f1+names

#unique
import numpy as np
list_all_unique = np.unique(np.array(list_all))
len(list_all_unique)

#extract list keys from model(test model with only 1000 items here)
science_dict = {}
not_found_item = []

print("start building science dictionary")

for science_key in list_all_unique:
    if science_key in model:
        science_dict[science_key] = model.get(science_key)
    else:
        not_found_item.append(science_key)

print("finished!",len(science_dict)," words founded!")
print(len(not_found_item)," words not found")
print(not_found_item)




#save the dictionary to D 

pickle_out = open("D:\\science1.pickle","wb")
pickle.dump(science_dict,pickle_out)
pickle_out.close()

print("Done. Pickle Saved.")
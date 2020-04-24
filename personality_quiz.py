
# questions = [ {1: "What type of tea are you?"}, 
#     {2: "If you were to go on a date, which one would you prefer?" }, 
#     {3: "What type of boba topping are you?"},
#     {4: "I prefer to wear...." },
#     {5: "What do you like doing on your free time?"},
#     {6: "What social media do you prefer?"},
#     {7: "Where is your dream trip?"},
#     {8: "What is your priority in the future?"},
#     {9: "What season do you prefer?"},
#     {10: "What would the scenic view of your future house be?"}
#     ]

# ### y-axis would be sexy (positive) and nerdy (negative)
# ### x-axis would be cute (negative) and mature (positive)

# answers = [
#     [{"a": "Oolong tea", "x": 1 }, {"b": "Strawberry Milk tea", "x": -1}, {"c": "Brown Sugar Milk tea", "y": 1}, {"d": "Grapefruit Green tea", "y": -1}],
#     [{"a": "Movie", "y": 1 }, {"b": "Ice skating", "x": 1}, {"c": "Museum", "y": -1}, {"d": "Amusement park", "x": -1}],
#     [{"a": "Cheese foam", "y": 1 }, {"b": "Nata jelly", "y": -1}, {"c": "Boba", "x": -1}, {"d": "Herbal Jelly", "x": 1}],
#     [{"a": "business casual", "x": 1 }, {"b": "Sweatpants", "y": -1}, {"c": "Skinny jeans", "y": 1}, {"d": "Skirt", "x": -1}],
#     [{"a": "Reading webtoons", "y": -1 }, {"b": "Yoga", "y": 1}, {"c": "Baking", "x": -1}, {"d": "Reading a book", "x": 1}],
#     [{"a": "LinkedIn", "x": 1 }, {"b": "Tik Tok", "y": 1}, {"c": "Facebook", "y": -1}, {"d": "Instagram", "x": -1}],
#     [{"a": "Tokyo", "x": -1 }, {"b": "Paris", "x": 1}, {"c": "Havana", "y": -1}, {"d": "Rome", "y": 1}],
#     [{"a": "Money", "y": -1 }, {"b": "Fame", "y": 1}, {"c": "Family", "x": 1}, {"d": "Love", "x": -1}],
#     [{"a": "Summer", "y": 1 }, {"b": "Spring", "x": -1}, {"c": "Fall", "x": 1}, {"d": "Winter", "y": -1}],
#     [{"a": "Garden", "x": -1 }, {"b": "Beach", "y": 1}, {"c": "Grassy land", "x": 1}, {"d": "City Skyline", "y": -1}],
#     ]


# print(questions[0][1])

# count = 0
# subcount = -1
# choices = ['a', 'b', 'c', 'd']
# for x in range(len(questions)):
#     count += 1
#     print(questions[x][count])
#     for y in range(4):
#         print(answers[x][y][choices[y]])

#     ##for v in answers[y]:
#             ##print(v)


# ### y-axis would be sexy (positive) and nerdy (negative)
# ### x-axis would be cute (negative) and mature (positive)



questions = [
    {
        "question":"What type of tea are you?",
        "answers":[
            {"answer": "Oolong tea", "orientation":"x", "value": 1},
            {"answer": "Strawberry Milk tea", "orientation": "x", "value": -1},
            {"answer": "Brown Sugar Milk tea", "orientation":"y", "value": 1},
            {"answer": "Grapefruit Green tea", "orientation": "y", "value": -1}
        ]
    },
    {
        "question":"If you were to go on a date, which one would you prefer?",
        "answers":[
            {"answer": "Amusement park", "orientation": "x", "value": -1},
            {"answer": "Ice skating", "orientation":"x", "value": 1},
            {"answer": "Museum", "orientation": "y", "value": -1},
            {"answer": "Movie", "orientation":"y", "value": 1}
        ]
    }
]

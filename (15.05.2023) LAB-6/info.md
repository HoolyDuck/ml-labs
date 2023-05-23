# model-1000-1000-350-15

## Characteristics:
- 150000 students
- for every 1500 students there is 
    - 350 good students; 
    - 15 priveleged students
- has two 1000 neurons layers
- was trained for 20 epochs with 50 batch size
- optimizer: Adam

## Results:
- 96.49% accuracy on test data
- test use - 1446/1500 students guessed correctly 
    - 6/15 priveleged students guessed correctly
    - 296/350 good students guessed correctly
- shows worse results when there are a lot of priveleged students (on 100 priveleged students it shows 94-95% accuracy)

# model-1500-1500-350-60.h5

## Characteristics:
- 300000 students
- for every 1500 students there is 
    - 350 good students; 
    - 60 priveleged students
- has two 1500 neurons layers
- was trained for 20 epochs with 100 batch size
- optimizer: Adam

## Results:
- 96.32% accuracy on test data
- test use - 1468/1500 students guessed correctly 
    - 70/100 priveleged students guessed correctly
    - 1398/1400 good students guessed correctly
- gets amount of students almost right, fails to guess priveleged students
- works better if there are 60 priveleged students (97-98% accuracy)

# model-1000-1000-350-random.h5

## Characteristics:
- 150000 students
- for every 1500 students there is 
    - 350 good students; 
    - 40-60 priveleged students
- has two 1000 neurons layers
- was trained for 20 epochs with 50 batch size
- optimizer: Adam

## Results:
- 91.89% accuracy on test data
- test use - 1354/1500 students guessed correctly 
    - 54/60 priveleged students guessed correctly
    - 1300/1440 good students guessed correctly
- terrible at guessing regular students, ok at guessing priveleged students


# model-1000-1000-1000-35-60.h5

accuracy: 0.9418

Priveleged right:  47
Priveleged wrong:  13
Non priveleged right:  1354
Non priveleged wrong:  86
Priveleged right accepted:  35
Non priveleged right accepted:  315
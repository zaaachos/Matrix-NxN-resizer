# Code Challenge from [Tech with Tim](https://discord.gg/K4pFxX) Discord Server
# The story
``Tim is creating a machine learning model that finds the presence of a circle in grayscale images. All of his training data is already preprocessed and the correct size, after training the model he sees it’s getting an accuracy of 100%! However, he is unable to use the model on any images that aren’t the same size as his training data, which are all images of size 64x64. Unfortunately, he can’t find any new images of that size to test his model with. In fact, the only images he can find are SQUARE and have a width and height that are factors of 64. He can find images of the following size: 32x32, 16x16, 8x8, 4x4, 2x2, 1x1. He needs a way to scale these images to the size 64x64 so that he can use them to test his model. Can you help him?``

# The task
> Write a function that takes an input matrix of size n x n where n is a factor of 64 and returns a new matrix that is of the size 64x64 and represents the original image. In other words, if we were to reverse this scaling operation we would be able to return to the original (smaller) image. You may assume all of these images will be grayscale and that the values for each pixel will be in the range 0-255. 
You are NOT allowed any third party libraries or modules.

### Example
To illustrate what is expected, have a look at how we scaled a 4x4 image to a 16x16 image.
4x4 Image
>[[1,2,3,4],
[5,6,7,8],
[9,10,11,12],
[13,14,15,16]]

16x16 Image
>[[1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4],
 [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4],
 [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4],
 [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4],
 [5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8],
 [5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8],
 [5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8],
 [5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8],
 [9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12],
 [9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12],
 [9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12],
 [9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12],
 [13, 13, 13, 13, 14, 14, 14, 14, 15, 15, 15, 15, 16, 16, 16, 16],
 [13, 13, 13, 13, 14, 14, 14, 14, 15, 15, 15, 15, 16, 16, 16, 16],
 [13, 13, 13, 13, 14, 14, 14, 14, 15, 15, 15, 15, 16, 16, 16, 16],
 [13, 13, 13, 13, 14, 14, 14, 14, 15, 15, 15, 15, 16, 16, 16, 16]]


And here is another example of scaling a 2x2 image to a 4x4.
2x2 Image
>[[1,2],
[3,4]]

4x4 Image
>[[1, 1, 2, 2], 
[1, 1, 2, 2], 
[3, 3, 4, 4], 
[3, 3, 4, 4]]

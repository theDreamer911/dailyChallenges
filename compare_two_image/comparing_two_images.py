# Importing the module
import cv2
import time

# My added function to make the program more better


def reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup


def pause():
    print("...")
    return time.sleep(1)


# Askikng for input
orign = input("Put the title of original image inside img directory: ")
check = input("Put the title of tested image inside img directory: ")

# Store the image into variable
original = cv2.imread(f"./img/{orign}")
duplicate = cv2.imread(f"./img/{check}")

# Store the image shape into variable
ori_shape = original.shape[:2]
dup_shape = duplicate.shape[:2]

# Store the rotation for the duplicate
rot_shape = reverse(dup_shape)

# Display the shape of the image
# print(original.shape)

print("\nChecking...\n")

# TEST 1: Based on shape of image
if ori_shape == dup_shape or ori_shape == rot_shape:
    print("Image size is same")
    pause()

    if ori_shape == dup_shape:
        print("Checking the color element")
        # Extract the difference of color element between two image
        difference = cv2.subtract(original, duplicate)
        b, g, r = cv2.split(difference)

        # TEST 2: Based on color of image
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            pause()
            print("The color is equal")
            pause()
            print("The image is identic")
            exit()
        else:
            pause()
            print('The color of image is different')
            cv2.imshow('Difference', difference)
    else:
        print("Image rotation is different")
        cv2.imshow('Duplicate', duplicate)

    pause()
    print("Image is different")
else:
    print("Image size is different")
    cv2.imshow("Duplicate",  duplicate)


cv2.waitKey(0)
cv2.destroyAllWindows()

def conv_check():
  # Write the solution array and call the function to verify it!
  solution = np.array([
                       [50, 150],
                       [0,   50]
                       ])

  original = np.array([
                       [0, 200, 200],
                       [0,   0, 200],
                       [0,   0,   0]
                       ])

  kernel = np.array([
                     [0.25, 0.25],
                     [0.25, 0.25]
                     ])

  actual_convolution = scipy.signal.correlate2d(original, kernel, mode="valid")

  if (solution == actual_convolution).all():
    print("✅ Your solution is correct!\n")
  else:
    print("❌ Your solution is incorrect.\n")

  return original, kernel, actual_convolution, solution


# add event to airtable
atform.add_event('Coding Exercise 2.1: Convolution of a Simple Kernel')

## Uncomment to test your solution!
original, kernel, actual_convolution, solution = conv_check()
with plt.xkcd():
  make_plots(original, actual_convolution, solution)
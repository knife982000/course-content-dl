def train_gan_iter(data, disc, gen):
  """Update the discriminator (`disc`) and the generator (`gen`) using `data`

  Args:
    data (ndarray): An array of shape (N,) that contains the data
    disc (Disc): The discriminator
    gen (Gen): The generator

  Returns:
  """

  # Number of samples in the data batch
  num_samples = 200

  # The data is the real samples
  x_real = data

  ## Discriminator training

  # Ask the generator to generate some fake samples
  x_fake = gen.sample(num_samples)

  # Compute the discriminator loss
  disc_loss = disc.loss(x_real, x_fake)

  # Compute the gradient for discriminator
  disc_grad = backprop(disc_loss, disc)

  # Update the discriminator
  update(disc, disc_grad)

  ## Generator training

  # Ask the generator to generate some fake samples
  x_fake = gen.sample(num_samples)

  # Compute the generator loss
  gen_loss = gen.loss(x_fake, disc.classify)

  # Compute the gradient for generator
  gen_grad = backprop(gen_loss, gen)

  # Update the generator
  update(gen, gen_grad)

  print("Your implementation passes the check!")

  return None


# add event to airtable
atform.add_event('Coding Exercise 1: The GAN training loop')

data = get_data()
disc = Disc()
gen = Gen()
## Uncomment below to check your function
train_gan_iter(data, disc, gen)
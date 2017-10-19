# Constants file
#
# SampleForSafeMDP and sampleForSafeMDPTU both use this file to instantiate constants.
# This means that you only have 1 place that both testing method use so you can more easily compare them.

# Safety threshold
h = -0.25

# Lipschitz
L = 0

# Scaling factor for confidence interval
beta = 2

# Define world
world_shape = (20, 20)
step_size = (0.5, 0.5)
# Parameterization Documentation

This project provides a software package for calculating the volume of a sphere using the Foo et al. parameterization.

## Installation

To install the Foo Parameterization package, you can use `pip`:

```bash
pip install .
```

## Usage

### Command Line Interface (CLI)

To calculate the volume of a sphere using the CLI, run the following command:

```bash
parameterization <radius>
```

Replace `<radius>` with the desired radius of the sphere. For example:

```bash
parameterization 3
```

This will calculate the volume of a sphere with a radius of 3 units.

### Python Module

You can also use the Foo Parameterization as a Python module in your own scripts. Here's how to use it:

```python
from calculate_volume import calculate_volume

radius = 3
volume = calculate_volume(radius)
print(f"Volume of sphere with radius {radius}: {volume}")
```

This will import the `calculate_volume` function from the module and use it to calculate the volume of a sphere with a radius of 3 units.

## Testing

To run the unit tests for this package, you can use the `unittest` module:

```bash
python -m unittest discover test
```

This will discover and run all the unit tests defined in the `test` directory.

# **Glare Reduction** - Image Processing

## Introduction

<img src="examples/first.jpg" alt="Glare reduction 1" />
<img src="examples/second.jpg" alt="Glare reduction 2" />

<b>Glare reduction</b> is a step in Recovering glare images by Image processing method in Convolutional Neural Network (CNN).

You can use this at step: <b>pre-processing data</b> in CNN.

<b>Glare reduction</b> includes 3-mixed-filter by 4 steps:

1. [Reduce-glare filter](#Reduce-glare-filter)
2. Enhance contract: f = 1.6
3. [Reduce-glare filter](#Reduce-glare-filter)
4. Enhance contract: f = 1.4

More details at `Documentation.pdf`

## Development

1. Put your glare image into `examples` folder.
2. In your terminal:

```sh
    python generate.py && python show_case.py
```

3. Check out your `Generated_Image` folder.

## Filters' Description

### <a name="Reduce-glare-filter"></a>1. Reduce-glare filter:

Include a 4-mixed-filter by 4 steps:

1. [First polynomial function](#first-func)
2. Gamma correction: g = 0.75
3. [Second polynomial function](#second-func)
4. Gamma correction: g = 0.8

### <a name="first-func"></a>2. First polynomial function:

For every pixel value within [0; 255], `First polynomial function` map it to another value so that:

- The intensity with value less than 100 will increase.
- The intensity with value greater than 100 will decrease.

<div style="text-align:center">
    <img src="examples/first_poly_func.png" width="350" alt="first poly func" /><br/>
    <i>Orange line<br/>x is original intensity<br/>y = f(x) is intensity after applying the first polynomial function</i>
</div>

`First polynomial function`'s expression:

<div style="text-align:center">
    <img src="examples/first_poly_exp.png" height="35" alt="first poly exp" />
</div>

### <a name="second-func"></a>3. Second polynomial function:

For every pixel value within [0; 255], `Second polynomial function` map it to another value so that:

- The intensity with value less than 160 will increase.
- The intensity with value greater than 160 will decrease.

<div style="text-align:center">
    <img src="examples/second_poly_func.png" width="350" alt="first poly func" /><br/>
    <i>Orange line<br/>x is original intensity<br/>y = f(x) is intensity after applying the second polynomial function</i>
</div>

`Second polynomial function`'s expression:

<div style="text-align:center">
    <img src="examples/second_poly_exp.PNG" height="35" alt="first poly exp" />
</div>

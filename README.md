# AsyncFlow Library #

## What is this? ##
Simple async module based on threading

## Quick Guide ##
The module provides you an easy way to create an async function without using default methods:

    
    @asyncflow.asynchronous
    def some_function(arr):
        time.sleep(1)
        
        for element in arr:
            print(element)
            time.sleep(0.1)

    some_function(['hello', 'easy', 'async', 'module'])

    >>>

    hello
    easy
    async
    module
    
Just use the decorator.


----------


### Using ###


Using the library is as simple and convenient as possible:

Let's import it first:
First, import everything from the library (use the `import asyncflow` construct).

The `wait` function is used to wait until an asynchronous function completes and returns its result.
It will block the current thread, or, if it is in an asynchronous function, pause it, waiting for the result.

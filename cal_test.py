from behave import *
import calc 
global result 


@given(u'we have have to test input string') 
def step_impl(context):
    pass 

@when(u'we have input string "99999"')
def step_impl(context): 
    global result
    result = calc.evaluate('99999')

@then(u'we will get result as 99999') 
def step_impl(context): 
    assert result == 99999 

@when(u'we have input string "---123"')
def step_impl(context): 
     global result
     result = calc.evaluate('---123')

@then(u'we will get result as -123') 
def step_impl(context):
     assert result == -123 

@when(u'we have input string "123.456"') 
def step_impl(context):
     global result
     result = calc.evaluate('123.456')

@then(u'we will get result as 123.456') 
def step_impl(context): 
    assert result == 123.456

@when(u'we have input string "0x10"')
def step_impl(context): 
    global result
    result = calc.evaluate('0x10') 
    
@then(u'we will get result as 16') 
def step_impl(context): 
    assert result == 16

@when(u'we have input string "1+1"') 
def step_impl(context): 
    global result
    result = calc.evaluate('1+1') 

@then(u'we will get result as 2') 
def step_impl(context): 
    assert result == 2
*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Go To Register Page
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click Button  Register
    Register Should Succeed


Register With Too Short Username And Valid Password
    Go to Register Page
    Set Username  x
    Set Password  asdf1234
    Set Password Confirmation  asdf1234
    Click Button  Register
    Register Should Fail With Message  Username must contain at least 3 characters

Register With Valid Username And Too Short Password
    Go to Register Page
    Set Username  xyz
    Set Password  asd123
    Set Password Confirmation  asd123
    Click Button Register
    Register Should Fail With Message  Password must contain at least 8 characters

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Go to Register Page
    Set Username  xyz
    Set Password  qwerasdf
    Set Password Confirmation  qwerasdf
    Click Button Register
    Register Should Fail With Message  Password must contain numbers or special characters

Register With Nonmatching Password And Password Confirmation
    Go to Register Page
    Set Username  xyz
    Set Password  asdf1234
    Set Password Confirmation  asdf1235
    Click Button Register
    Register Should Fail With Message  Passwords don't match!

Register With Username That Is Already In Use
    Go to Register Page
    Set Username  xyz
    Set Password  asdf1234
    Set Password Confirmation  asdf1234
    Click Button Register
    Register Should Succeed
    Go to Register Page
    Set Username  xyz
    Set Password  asdf4321
    Set Password Confirmation  asdf4321
    Click Button Register
    Register Should Fail With Message  Username already exists


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

*** Keywords ***

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Go To Register Page
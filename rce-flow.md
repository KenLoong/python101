sequenceDiagram
participant Attacker
participant WebApp
participant EJS as Template Engine
participant RCE as Child Process
participant Webhook

    Attacker->>WebApp: Send form data with key=`__proto__.toString` and EJS payload
    WebApp->>WebApp: Assign userInput to baseIngredients (Prototype Pollution)
    WebApp->>EJS: Render template with baseIngredients
    EJS->>Object.prototype: Access polluted toString()
    Object.prototype->>RCE: Execute injected code via child_process.exec
    RCE->>Webhook: HTTP POST /flag.txt
    Webhook-->>Attacker: Flag data received

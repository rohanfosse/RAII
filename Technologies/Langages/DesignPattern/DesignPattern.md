# Design Patterns

## Introduction

Design patterns are recurring solutions to software design problems. They are used to make code more flexible, reusable, and maintainable. They also help to make code more readable and cleaner. Design patterns can be classified into three main categories:

- **Creational**: These patterns deal with the object creation process. They help make a system independent of how its objects are created, composed, and represented.

- **Structural**: These patterns deal with how classes and objects are composed to form larger structures.

- **Behavioral**: These patterns deal with how objects interact and distribute responsibility.

## Creational Patterns

### Singleton

The Singleton pattern ensures that a class has only one instance and provides a global access point to this instance. It is used in cases where only one instance of a class is needed throughout the program. For example, a logging class that writes messages to a file or a database. It's important to note that the Singleton pattern does not guarantee thread safety. There are several ways to implement the Singleton pattern in C#:

- **Lazy**: The Singleton class is instantiated when the `GetInstance()` method is called for the first time.

```csharp
public sealed class Singleton
{
    private static Singleton instance = null;

    private Singleton()
    {
    }

    public static Singleton Instance
    {
        get
        {
            if (instance == null)
            {
                instance = new Singleton();
            }
            return instance;
        }
    }
}
```

- **Thread-safe**: The Singleton class is instantiated at the first call to the `GetInstance()` method. The method is marked as `synchronized` to ensure thread safety.

```csharp
public sealed class Singleton
{
    private static Singleton instance = null;
    private static readonly object padlock = new object();

    private Singleton()
    {
    }

    public static Singleton Instance
    {
        get
        {
            lock (padlock)
            {
                if (instance == null)
                {
                    instance = new Singleton();
                }
                return instance;
            }
        }
    }
}
```

- **Eager**: The Singleton class is instantiated when the class is loaded.

```csharp
public sealed class Singleton
{
    private static readonly Singleton instance = new Singleton();

    static Singleton()
    {
    }

    private Singleton()
    {
    }

    public static Singleton Instance
    {
        get
        {
            return instance;
        }
    }
}
```

### Factory

The Factory pattern is used to create objects without specifying the exact class of the object that will be created. This is done by calling a common creation method to create objects. It is used in cases where a class does not know what subclasses will need to be created. For example, a logging class that can write messages to a file or a database. There are several ways to implement the Factory pattern in C#:

- **Simple**: The Factory class is implemented using a static method that creates and returns objects.

```csharp
public class Factory
{
    public static Product GetProduct(string type)
    {
        switch (type)
        {
            case "A":
                return new ProductA();
            case "B":
                return new ProductB();
            default:
                throw new ArgumentException("Invalid type.", "type");
        }
    }
}
```

- **Method**: The Factory class is implemented using a virtual method to create and return objects.

```csharp
public abstract class Factory
{
    public abstract Product GetProduct();

    public static Factory GetFactory(string type)
    {
        switch (type)
        {
            case "A":
                return new FactoryA();
            case "B":
                return new FactoryB();
            default:
                throw new ArgumentException("Invalid type.", "type");
        }
    }
}
```

### Observer

The Observer pattern is used to define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically. It is used in cases where an object needs to be notified when another object changes state. For example, an object displaying data in a graphical user interface needs to be notified when the data changes to update the UI. There are several ways to implement the Observer pattern in C#:

- **Push**: The Observable object sends data to the Observer object when it changes state.

```csharp
public class Observable
{
    private List<Observer> observers = new List<Observer>();

    public void Attach(Observer observer)
    {
        observers.Add(observer);
    }

    public void Detach(Observer observer)
    {
        observers.Remove(observer);
    }

    public void Notify()
    {
        foreach (Observer observer in observers)
        {
            observer.Update(this);
        }
    }
}

public class Observer
{
    public void Update(Observable observable)
    {
        // ...
    }
}
```

- **Pull**: The Observer object requests data from the Observable object when it changes state.

```csharp
public class Observable
{
    private List<Observer> observers =

 new List<Observer>();

    public void Attach(Observer observer)
    {
        observers.Add(observer);
    }

    public void Detach(Observer observer)
    {
        observers.Remove(observer);
    }

    public void Notify()
    {
        foreach (Observer observer in observers)
        {
            observer.Update();
        }
    }

    public string GetData()
    {
        // ...
    }
}

public class Observer
{
    public void Update()
    {
        string data = observable.GetData();
        // ...
    }
}
```

## Structural Patterns

### Strategy

The Strategy pattern is used to define a family of algorithms, encapsulate each one, and make them interchangeable. It is used in cases where an algorithm needs to be selected dynamically from a set of algorithms. For example, a sorting algorithm that can be selected dynamically among bubble sort, insertion sort, and quick sort algorithms. There are several ways to implement the Strategy pattern in C#:

- **Simple**: The Context class is implemented using a property that sets the algorithm to use.

```csharp
public class Context
{
    private IStrategy strategy;

    public Context(IStrategy strategy)
    {
        this.strategy = strategy;
    }

    public void SetStrategy(IStrategy strategy)
    {
        this.strategy = strategy;
    }

    public void ExecuteStrategy()
    {
        strategy.Execute();
    }
}

public interface IStrategy
{
    void Execute();
}

public class StrategyA : IStrategy
{
    public void Execute()
    {
        // ...
    }
}

public class StrategyB : IStrategy
{
    public void Execute()
    {
        // ...
    }
}
```

- **Advanced**: The Context class is implemented using a virtual method that sets the algorithm to use.

```csharp
public abstract class Context
{
    public abstract void ExecuteStrategy();
}

public class ContextA : Context
{
    public override void ExecuteStrategy()
    {
        // ...
    }
}

public class ContextB : Context
{
    public override void ExecuteStrategy()
    {
        // ...
    }
}
```

### Bridge

The Bridge pattern is used to separate an abstraction from its implementation so that the two can vary independently. It is used in cases where an abstraction needs to be extended in two dimensions. For example, a shape class that can be extended by a color class and a drawing class. There are several ways to implement the Bridge pattern in C#:

- **Simple**: The Abstraction class is implemented using a property that sets the implementation to use.

```csharp
public abstract class Abstraction
{
    protected IImplementation implementation;

    public Abstraction(IImplementation implementation)
    {
        this.implementation = implementation;
    }

    public void SetImplementation(IImplementation implementation)
    {
        this.implementation = implementation;
    }

    public abstract void Execute();
}

public interface IImplementation
{
    void Execute();
}

public class ImplementationA : IImplementation
{
    public void Execute()
    {
        // ...
    }
}

public class ImplementationB : IImplementation
{
    public void Execute()
    {
        // ...
    }
}
```

- **Advanced**: The Abstraction class is implemented using a virtual method that sets the implementation to use.

```csharp
public abstract class Abstraction
{
    protected IImplementation implementation;

    public Abstraction(IImplementation implementation)
    {
        this.implementation = implementation;
    }

    public void SetImplementation(IImplementation implementation)
    {
        this.implementation = implementation;
    }

    public abstract void Execute();
}

public interface IImplementation
{
    void Execute();
}

public class ImplementationA : IImplementation
{
    public void Execute()
    {
        // ...
    }
}

public class ImplementationB : IImplementation
{
    public void Execute()
    {
        // ...
    }
}
```

## Behavioral Patterns

### Command

The Command pattern is used to encapsulate a request as an object, thereby allowing for parameterization of clients with queues, requests, and operations. It also allows for undoable operations. It's used in cases where operations need to be executed or undone at different times, or when the execution of an operation depends on certain conditions. The Command pattern decouples the object that invokes the operation from the one that knows how to perform it.

Here's how to implement the Command pattern in C#:

- **Basic Implementation**: A command interface defines the `Execute` method, and concrete command classes implement this method. A `CommandInvoker` class is used to trigger these commands.

```csharp
public interface ICommand
{
    void Execute();
}

public class ConcreteCommandA : ICommand
{
    private Receiver receiver;

    public ConcreteCommandA(Receiver receiver)
    {
        this.receiver = receiver;
    }

    public void Execute()
    {
        receiver.ActionA();
    }
}

public class ConcreteCommandB : ICommand
{
    private Receiver receiver;

    public ConcreteCommandB(Receiver receiver)
    {
        this.receiver = receiver;
    }

    public void Execute()
    {
        receiver.ActionB();
    }
}

public class Receiver
{
    public void ActionA()
    {
        // Implementation of action A
    }

    public void ActionB()
    {
        // Implementation of action B
    }
}

public class CommandInvoker
{
    private ICommand command;

    public void SetCommand(ICommand command)
    {
        this.command = command;
    }

    public void ExecuteCommand()
    {
        command.Execute();
    }
}
```

- **Advanced Implementation with Undo Capability**: This extends the basic implementation to support undoable operations. Each command class implements an `Undo` method.

```csharp
public interface ICommand
{
    void Execute();
    void Undo();
}

// Concrete commands and Receiver class similar to the basic implementation

public class CommandInvoker
{
    private Stack<ICommand> commandHistory = new Stack<ICommand>();

    public void ExecuteCommand(ICommand command)
    {
        command.Execute();
        commandHistory.Push(command);
    }

    public void Undo()
    {
        if (commandHistory.Count > 0)
        {
            ICommand command = commandHistory.Pop();
            command.Undo();
        }
    }
}
```

### State

The State pattern is used to alter the behavior of an object when its internal state changes. This pattern is used in cases where the behavior of an object depends on its state and it must be able to change its behavior at runtime according to its internal state.

Here's a basic example in C#:

```csharp
public interface IState
{
    void Handle(Context context);
}

public class ConcreteStateA : IState
{
    public void Handle(Context context)
    {
        Console.WriteLine("Handling state A");
        context.State = new ConcreteStateB();
    }
}

public class ConcreteStateB : IState
{
    public void Handle(Context context)
    {
        Console.WriteLine("Handling state B");
        context.State = new ConcreteStateA();
    }
}

public class Context
{
    public IState State { get; set; }

    public Context(IState state)
    {
        State = state;
    }

    public void Request()
    {
        State.Handle(this);
    }
}
```

In this pattern, the `Context` class contains a reference to an instance of a class that implements the `IState` interface, which represents the current state. The state's `Handle` method is responsible for performing actions associated with that state and for transitioning to the next state.

## Practical Examples

### Creational Patterns

#### Singleton

- **Logging**: A logging class is often implemented as a Singleton to ensure that a single log file is used throughout an application.
- **Database Connections**: Managing a database connection or a connection pool as a Singleton can help in maintaining a consistent state and managing resources efficiently.
- **Configuration Settings**: A Singleton can be used to load and provide access to configuration settings that are used application-wide.

#### Factory

- **User Interface Components**: In a GUI application, a factory can be used to create different types of UI elements (buttons, text boxes, etc.) based on user input or context.
- **Support for Multiple Database Types**: If an application needs to support multiple database types (SQL Server, Oracle, etc.), a factory can provide the appropriate database connection based on a configuration file or user selection.

### Structural Patterns

#### Strategy

- **Payment Processing**: An e-commerce application might use the Strategy pattern to handle different payment methods (credit card, PayPal, etc.) where each method has its own algorithm for processing payments.
- **Data Compression**: In a file compression tool, different compression algorithms (ZIP, RAR, etc.) can be implemented as strategies, allowing the user to choose how to compress files.

#### Bridge

- **Device Drivers**: A software that interacts with different types of printers might use the Bridge pattern. The abstraction layer represents a generic printer, and the implementation layer provides specifics for each printer type.
- **User Interface Themes**: In a UI framework, the Bridge pattern can separate an abstraction (like a window) from its appearance (theme). This allows the same window logic to work with different themes.

### Behavioral Patterns

#### Command

- **GUI Buttons and Menu Items**: In graphical user interfaces, each button or menu item can be associated with a Command object that encapsulates the action to be performed.
- **Undo/Redo Operations**: In text editors or graphic design software, commands represent actions like 'copy', 'paste', etc., and can provide support for undo/redo functionality.

#### State

- **Order Management Systems**: In e-commerce systems, an order can be in various states (New, Approved, Delivered, Cancelled). The State pattern can manage state-specific logic such as transitioning an order from New to Approved.

#### Observer

- **Event Management Systems**: In GUI applications or event-driven architectures, the Observer pattern is used for implementing event handling systems where subscribers are notified when an event (like a button click) occurs.
- **Stock Market Feed**: In a stock market application, the Observer pattern can be used to notify traders or algorithms when stock prices change.

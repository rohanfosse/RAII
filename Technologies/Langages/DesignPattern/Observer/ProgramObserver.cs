
class ProgramObserver
{
    static void Main(string[] args)
    {
        // Create subject
        var subject = new ConcreteSubject();

        // Create observers
        var observerA = new ConcreteObserver();
        var observerB = new ConcreteObserver();

        // Attaching observers to subject
        subject.Attach(observerA);
        subject.Attach(observerB);

        // Change state of subject
        subject.State = "State 1";

        // Detach an observer and update state
        subject.Detach(observerA);
        subject.State = "State 2";
    }
}

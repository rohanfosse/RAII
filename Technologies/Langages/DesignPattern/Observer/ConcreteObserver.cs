
using System;

public class ConcreteObserver : IObserver
{
    public void Update(ISubject subject)
    {
        if (subject is ConcreteSubject concreteSubject)
        {
            Console.WriteLine("ConcreteObserver: Reacted to the event. State is now: " + concreteSubject.State);
        }
    }
}

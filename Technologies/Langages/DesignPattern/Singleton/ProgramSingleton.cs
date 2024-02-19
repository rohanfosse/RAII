
class singletonProgram
{
    static void Main(string[] args)
    {
        // Accessing the singleton instance and using its method to log a message
        Logger.Instance.Log("Application has started.");

        // Perform other operations...

        Logger.Instance.Log("Application is running.");

        // Perform other operations...

        Logger.Instance.Log("Application is shutting down.");
    }
}

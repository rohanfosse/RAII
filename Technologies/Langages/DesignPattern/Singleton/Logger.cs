
public class Logger
{
    // Static variable that holds the single instance of the class
    private static Logger instance = null;

    // Private constructor to prevent external instantiation
    private Logger()
    {
        // Initialization, if necessary, goes here
    }

    // Public static method to get the instance of the class
    public static Logger Instance
    {
        get
        {
            if (instance == null)
            {
                instance = new Logger();
            }
            return instance;
        }
    }

    // Example method for logging a message
    public void Log(string message)
    {
        // Log message to the console
        Console.WriteLine("[LOG] " + message);
    }
}

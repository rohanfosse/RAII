
class ProgramFactory
{
    static void Main(string[] args)
    {
        VehicleFactory factory = new VehicleFactory();

        IVehicle myCar = factory.GetVehicle("car");
        myCar.DescribeVehicle();

        IVehicle myTruck = factory.GetVehicle("truck");
        myTruck.DescribeVehicle();

        IVehicle myBicycle = factory.GetVehicle("bicycle");
        myBicycle.DescribeVehicle();
    }
}

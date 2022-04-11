import java.util.Scanner;
import java.util.Vector;

class InventoryCLI {
    public static void main(String args[]) {
        Scanner command = new Scanner(System.in);
        Vector<Item> table = new Vector<Item>();
    
        loop: while (true) {
            
            String name;
            int code, units;
            float price;
            
            if (table.size() > 0) {
                printTable(table);
            } else {
                System.out.println("No items in inventory.");
            }
            System.out.println();

            System.out.println("[0] TERMINATE PROGRAM");
            System.out.println("[1] UPDATE UNITS");
            System.out.println("[2] UPDATE PRICE");
            System.out.println("[3] ADD ITEM");

            System.out.print("Enter command: ");
            switch(command.nextLine()) {
                case "0":
                    System.out.println("Program terminated.");
                    break loop;
                case "1":
                    code = Integer.parseInt(prompt("Enter item code:"));
                    units = Integer.parseInt(prompt("Enter new no. of units:"));

                    for (Item item : table) {
                        if ( item.getCode() == code ) {
                            item.setUnits(item.getUnits() + units);
                            System.out.println("Item's no. of units updated.");
                            break;
                        }
                    }
                    break;
                case "2":
                    code = Integer.parseInt(prompt("Enter item code:"));
                    price = Float.parseFloat(prompt("Enter new price: "));

                    for (Item item : table) {
                        if (item.getCode() == code) {
                            item.setPrice(price);
                            System.out.println("Item's price updated.");
                            break;
                        }
                    }
                    break;
                case "3":
                    code = table.size();
                    name = prompt("Enter item name: ");
                    units = Integer.parseInt(prompt("Enter no. of units: "));
                    price = Float.parseFloat(prompt("Enter new price: "));
                    table.add(new Item(code, name, units, price));
            }

            System.out.println();
        }
    }

    public static String prompt(String query) {
        System.out.print(query);
        Scanner input = new Scanner(System.in);
        return input.nextLine();
    }

    public static void printTable(Vector<Item> table) {
        System.out.println(String.format("%15s%15s%15s%15s", "Code", "Name", "Units", "Price"));

        for (Item item : table) {
            int code = item.getCode();
            String name = item.getName();
            int units = item.getUnits();
            float price = item.getPrice();

            System.out.println(String.format("%15s%15s%15s%15s", code, name, units, price));
        }
    }

}

class Item {
    private int code;
    private String name;
    private int units;
    private float price;

    Item(int code, String name, int units, float price) {
        this.code = code;
        this.name = name;
        this.units = units;
        this.price = price;
    }

    public int getCode() {
        return code;
    }

    public int setCode(int code) {
        this.code = code;
        return code;
    }

    public String getName() {
        return name;
    }

    public String setName(String name) {
        this.name = name;
        return name;
    }

    public int getUnits() {
        return units;
    }

    public int setUnits(int units) {
        this.units = units;
        return units;
    }

    public float getPrice() {
        return price;
    }

    public float setPrice(float price) {
        this.price = price;
        return price;
    }
}
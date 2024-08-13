import java.util.ArrayList;
import java.util.Collections;

public class Arraylists {
    public static void main(String args[]) {
        // Integer | Float | Boolean
        ArrayList<Integer> list = new ArrayList<Integer>();

        // Add elements
        list.add(0);
        list.add(2);
        list.add(3);

        System.out.println(list);

        // Get elements
        int element = list.get(0);
        System.out.println(element);

        // add element in between
        list.add(1, 1);
        System.out.println(list);

        // set element
        list.set(0, 5);
        System.out.println(list);

        //Delete
        list.remove(3);
        System.out.println(list);

        // Size
        int size = list.size();
        System.out.println(size);

        // loops
        for (int i=0; i < list.size(); i++) {
            System.out.println(list.get(i));
        }
        System.out.println();

        /*Sorting
         * Collections is a class that have method  called "Sort"
         */
        Collections.sort(list);
        System.out.println(list);
    }
}

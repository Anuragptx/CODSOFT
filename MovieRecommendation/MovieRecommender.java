import java.util.*;

public class MovieRecommender {

    static class Film {
        String name;
        ArrayList<String> genres;

        Film(String name, String... genres) {
            this.name = name;
            this.genres = new ArrayList<>();

            for (String g : genres) {
                this.genres.add(g);
            }
        }
    }

    public static double similarity(Film a, Film b) {

        int common = 0;

        for (int i = 0; i < a.genres.size(); i++) {
            for (int j = 0; j < b.genres.size(); j++) {
                if (a.genres.get(i).equals(b.genres.get(j))) {
                    common++;
                }
            }
        }

        int total = a.genres.size() + b.genres.size() - common;

        if (total == 0) return 0;

        return (double) common / total;
    }

    public static ArrayList<String> recommend(Film[] arr, String movie) {

        Film target = null;

        // find target movie
        for (int i = 0; i < arr.length; i++) {
            if (arr[i].name.equalsIgnoreCase(movie)) {
                target = arr[i];
                break;
            }
        }

        if (target == null) {
            System.out.println("Movie not found!");
            return new ArrayList<>();
        }

        double[] score = new double[arr.length];

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] != target) {
                score[i] = similarity(target, arr[i]);
            } else {
                score[i] = -1;
            }
        }

        ArrayList<String> result = new ArrayList<>();
        for (int k = 0; k < 3; k++) {

            double max = -1;
            int index = -1;

            for (int i = 0; i < arr.length; i++) {
                if (score[i] > max) {
                    max = score[i];
                    index = i;
                }
            }

            if (index != -1) {
                result.add(arr[index].name);
                score[index] = -1;
            }
        }

        return result;
    }
    public static void main(String[] args) {

        Film[] arr = {
                new Film("Inception", "sci-fi", "thriller"),
                new Film("Interstellar", "sci-fi", "space", "drama"),
                new Film("Matrix", "sci-fi", "action"),
                new Film("Prestige", "drama", "mystery"),
                new Film("Dark Knight", "action", "crime")
        };

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter movie name: ");
        String movie = sc.nextLine();

        ArrayList<String> ans = recommend(arr, movie);

        System.out.println("\nRecommended Movies:");

        for (String s : ans) {
            System.out.println("- " + s);
        }

        sc.close();
    }
}
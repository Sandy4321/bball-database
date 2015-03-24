import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;
import java.util.ArrayList;

public class ScrapeBall {
    public static ArrayList<Element> pg = new ArrayList<Element>();
    public static ArrayList<Element> sg = new ArrayList<Element>();
    public static ArrayList<Element> sf = new ArrayList<Element>();
    public static ArrayList<Element> pf = new ArrayList<Element>();
    public static ArrayList<Element> c = new ArrayList<Element>();
    public static int pointIndex = 28;
    public static int foulsIndex = 27;
    public static int tovIndex = 26;
    public static int blkIndex = 25;
    public static int stlIndex = 24;
    public static int astIndex = 23;
    public static int tRebIndex = 22;
    public static int dRebIndex = 21;
    public static int oRebIndex = 20;
    public static int ftaIndex = 18;
    public static int ftmIndex = 17;
    public static int twoPtAttIndex = 15;
    public static int twoPtMadeIndex = 14;
    public static int threePtAttIndex = 12;
    public static int threePtMadeIndex = 11;
    public static int fgAttIndex = 9;
    public static int fgMadeIndex = 8;
    public static int minIndex = 7;
    public static int ageIndex = 3;
    public static int posIndex = 2;

    public static void main(String[] args) throws IOException {
        Document doc = Jsoup.connect("http://www.basketball-reference.com/leagues/NBA_2014_per_minute.html").get();
        Element t = doc.getElementById("per_minute");
        Elements table = t.getElementsByClass("full_table");
        // System.out.println(table);
        // int size = 0;
        for (int x = 0; x < table.size(); x++) {
            Element tableData = table.get(x);
            addPlayerByPos(tableData, getPos(tableData));
        }
        double avgPoints = getAverage(pg, astIndex);
        System.out.println(avgPoints);
    }

    public static String getPos(Element e) {
        Elements td = e.getElementsByTag("td");
        String pos = td.get(posIndex).html();
        return pos;
    }

    public static void addPlayerByPos(Element e, String pos) {
        String p = getPos(e);
        if (p.equals(pos)) {
            if (pos.equals("PG")) pg.add(e);
            if (pos.equals("SG")) sg.add(e);
            if (pos.equals("SF")) sf.add(e);
            if (pos.equals("PF")) pf.add(e);
            if (pos.equals("C")) c.add(e);
        }
    }
    public static double getStat(Element e, int index) {
        Elements td = e.getElementsByTag("td");
        double stat = Double.parseDouble(td.get(index).html());
        return stat;
    }
    public static double getAverage(ArrayList<Element> posList, int index) {
        double stats = 0.0;
        double avg = 0.0;
        for (int i = 0; i < posList.size(); i++) {
            Element player = posList.get(i);
            stats += getStat(player, index);
        }
        avg = stats/posList.size();
        return avg;
    }

    // Gets highest stat
    // Gets 12% minute filtered set
}
//----------------------------------------------------------//
// Tarefa 03: Implementar e Testar Fórmulas de Newton-Cotes //  
// Grupo 19:  Adriano Gadelha                               //
//            Ricardo Victor                                //
//----------------------------------------------------------//
//                        ABERTo                            //
//----------------------------------------------------------//
public class Aberto {
    public static void main(String[] args) {
        double[] firstResults = doPartition(1, 1, 0, 0.00001);
        double[] secondResults = doPartition(2, 1, 0, 0.00001);
        double[] thirdResults = doPartition(3, 1, 0, 0.00001);
        double[] fourthResults = doPartition(4, 1, 0, 0.00001);

        System.out.println("Newton-Cotes ABERTO\n");
        
        System.out.println("Função: (sen(2x) + 4x² + 3x)²\n");
        System.out.println("ε = 0.00001, Low = 0, High = 1\n");

        System.out.println("Resultado grau 1:\n");
        System.out.println(firstResults[0]+"\n");
        System.out.println("Número de iterações:\n");
        System.out.println(firstResults[1]+"\n");

        System.out.println("Resultado grau 2:\n");
        System.out.println(secondResults[0]+"\n");
        System.out.println("Número de iterações:\n");
        System.out.println(secondResults[1]+"\n");

        System.out.println("Resultado grau 3:\n");
        System.out.println(thirdResults[0]+"\n");
        System.out.println("Número de iterações:\n");
        System.out.println(thirdResults[1]+"\n");

        System.out.println("Resultado grau 4:\n");
        System.out.println(fourthResults[0]+"\n");
        System.out.println("Número de iterações:\n");
        System.out.println(fourthResults[1]+"\n");

    }

    public static double thisFunction(double x) {
        // (sen(2x) + 4x² + 3x)²
        double y = Math.pow(Math.sin(2*x) + (Math.pow(x, 2) * 4) + (3*x), 2);
        return y;
    }

    public static double[] doPartition(int degree, double high, double low, double limit) {

        int i_count = 0;
    
        double i_val = 0.1;
        double prior_val = 1000;
        
        double i_x;
        double x;
    
        double partitions = 1;
        
        double delta_x;
        double sum;
    
        while (Math.abs((i_val - prior_val) / i_val) > limit) {
            i_count++;
    
            partitions = 2 * partitions;
            delta_x = (high - low) / partitions;
            sum = 0;
    
            for (int i = 0; i < partitions; i++) {
                x = low + i * delta_x;
                i_x = x + delta_x;
                sum = sumIntegral(sum, degree, high, low);
            }
    
            prior_val = i_val;
            i_val = sum;
        }

        double[] results = {i_val, i_count};
    
        return results;
    }

    
    private static double sumIntegral(double result, int degree, double high, double low) {
        switch (degree) {
            case 1:
                result = result + first(high, low);
    
                break;

            case 2:
                result = result + second(high, low);
    
                break;

            case 3:
                result = result + third(high, low);
    
                break;

            case 4:
                result = result + forth(high, low);
    
                break;
            
            default:
                break;
        }
        return result;
    }

    public static double first(double high, double low) {

        double f0;
        double f1;
        double f2;
        double f3;

        double delta_x;
        double result;

        delta_x = (high - low);
        
        f0 = thisFunction(low);
        f1 = thisFunction(low + delta_x / 3);
        f2 = thisFunction(low + delta_x * 2 / 3);
        f3 = thisFunction(high);

        result = (delta_x / 2) * (0 * f0 + f1 + f2 + 0 * f3);

        return result;
    }

    public static double second(double high, double low) {

        double f0;
        double f1;
        double f2;
        double f3;
        double f4;
        
        double result;
        double delta_x;

        delta_x = (high - low);
        
        f0 = thisFunction(low);
        f1 = thisFunction(low + delta_x / 4);
        f2 = thisFunction(low + delta_x / 2);
        f3 = thisFunction(low + delta_x * 3 / 4);
        f4 = thisFunction(high);
        
        result = (delta_x / 3) * (0 * f0 + 2 * f1 - 1 * f2 + 2 * f3 + 0 * f4);

        return result;
    }

    public static double third(double high, double low) {

        double f0;
        double f1;
        double f2;
        double f3;
        double f4;
        double f5;
        
        double result;
        double delta_x;

        delta_x = (high - low);
        
        f0 = thisFunction(low);
        f1 = thisFunction(low + delta_x / 5);
        f2 = thisFunction(low + delta_x * 2 / 5);
        f3 = thisFunction(low + delta_x * 3 / 5);
        f4 = thisFunction(low + delta_x * 4 / 5);
        f5 = thisFunction(high);
        
        result = (delta_x / 24) * (0 * f0 + 11 * f1 + 1 * f2 + 1 * f3 + 11 * f4 + 0 * f5);

        return result;
    }

    public static double forth(double high, double low) {

        double f0;
        double f1;
        double f2;
        double f3;
        double f4;
        double f5;
        double f6;
        
        double result;
        double delta_x;

        delta_x = (high - low);
        
        f0 = thisFunction(low);
        f1 = thisFunction(low + delta_x / 6);
        f2 = thisFunction(low + delta_x / 3);
        f3 = thisFunction(low + delta_x / 2);
        f4 = thisFunction(low + delta_x * 2 / 3);
        f5 = thisFunction(low + delta_x * 5 / 6);
        f6 = thisFunction(high);
        
        result = (delta_x / 20) * (0 * f0 + 11 * f1 - 14 * f2 + 26 * f3 - 14 * f4 + 11 * f5 + 0 * f6);

        return result;
    }
}
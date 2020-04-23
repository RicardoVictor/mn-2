//----------------------------------------------------------//
// Tarefa 03: Implementar e Testar Fórmulas de Newton-Cotes //  
// Grupo 19:  Adriano Gadelha                               //
//            Ricardo Victor                                //
//----------------------------------------------------------//
//                        FECHADO                           //
//----------------------------------------------------------//
public class Fechado {
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
	
	public static double second(double high, double low) {
		double f1;
	    double f2;
	    double f3;
	    double result;
	    double delta_x;

	    delta_x = (high - low);
	    f1 = thisFunction(low);
	    f2 = thisFunction((low + high)/2);
	    f3 = thisFunction(high);
	    result = (delta_x/6)*(f1 + 4*f2 + f3);

	    return result;
	}
	
	
	public static double third(double high, double low) {
	    double f1;
	    double f2;
	    double f3;
	    double f4;
	    double result;
	    double delta_x;

	    delta_x = (high - low);
	    f1 = thisFunction(low);
	    f2 = thisFunction(low + delta_x/3);
	    f3 = thisFunction(low + delta_x*2/3);
	    f4 = thisFunction(high);
	    result = (delta_x*3/24)*(f1 + 3*f2 + 3*f3 + f4);

	    return result;
	}
	
	public static double forth(double high, double low) {
	    double f1;
	    double f2;
	    double f3;
	    double f4;
	    double f5;
	    double result;
	    double delta_x;

	    delta_x = (high - low);
	    f1 = thisFunction(low);
	    f2 = thisFunction(low + delta_x/4);
	    f3 = thisFunction(low + delta_x/2);
	    f4 = thisFunction(low + delta_x*3/4);
	    f5 = thisFunction(high);
	    result = (delta_x/90)*(7*f1 + 32*f2 + 12*f3 + 32*f4 + 7*f5);

	    return result;
	}
	
	public static double[] doPartition(int degree, double high, double low, double limit) {

        int i_count = 0;

	    double i_val = 0.1;
        double prior_val = 1000;
        
	    double x;
	    double i_x;
	    double x_p;
        
        double partitions = 1;
        
	    double delta_x;
	    double sum;

	    while(Math.abs((i_val - prior_val)/i_val) > limit) {
            i_count++;

	        partitions = 2*partitions;
	        delta_x = (high - low)/partitions;
	        sum = 0;

	        for (int i=0; i<partitions; i++) {
	            x = low + i*delta_x;
	            i_x = x + delta_x;

				switch (degree) {
				case 0:
					x_p = low + delta_x * i;
					sum = sum + delta_x * thisFunction(x_p);

					break;

				case 1:
					i_x = low + i * delta_x;
					sum = sum + delta_x * (thisFunction(i_x) + thisFunction(i_x + delta_x)) / 2;

					break;

				case 2:
					sum = sum + second(i_x, x);

					break;

				case 3:
					sum = sum + third(i_x, x);
					break;

				case 4:
					sum = sum + forth(i_x, x);
					break;

				}

			}

	        prior_val = i_val;
	        i_val = sum;
        }
        double[] results = {i_val, i_count};
	    return results;
	}
}
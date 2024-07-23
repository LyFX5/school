package custom;

import java.util.Arrays;
import java.util.Random;
import java.util.function.BinaryOperator;
import java.util.function.Supplier;
import java.util.function.UnaryOperator;
import java.util.stream.IntStream;

import org.knowm.xchart.QuickChart;
import org.knowm.xchart.SwingWrapper;
import org.knowm.xchart.XYChart;
import org.uma.jmetal.algorithm.Algorithm;
import org.uma.jmetal.algorithm.singleobjective.geneticalgorithm.GeneticAlgorithmBuilder;
import org.uma.jmetal.operator.crossover.CrossoverOperator;
import org.uma.jmetal.operator.mutation.MutationOperator;
import org.uma.jmetal.problem.Problem;
import org.uma.jmetal.solution.Solution;
import org.uma.jmetal.util.evaluator.SolutionListEvaluator;
import org.uma.jmetal.util.evaluator.impl.MultiThreadedSolutionListEvaluator;

import common.ErrorLoggingFunction;
import numeric.Rastrigin;

public class Example {

	public static <T> T runGA(Problem<Solution<T>> problem, BinaryOperator<T> crossover, 
			                  UnaryOperator<T> mutation, int limit, int numberOfCores) {
		
		SolutionListEvaluator<Solution<T>> evaluator = 
				new MultiThreadedSolutionListEvaluator<Solution<T>>(numberOfCores);

		CrossoverOperator<Solution<T>> crossoverOperator = new CustomCrossover<>(crossover, 0.9);
		MutationOperator<Solution<T>> mutationOperator = new CustomMutation<>(mutation, 0.9);

		GeneticAlgorithmBuilder<Solution<T>> builder = new GeneticAlgorithmBuilder<Solution<T>>
				(problem, crossoverOperator, mutationOperator);
		
		builder.setMaxEvaluations(limit);
		builder.setSolutionListEvaluator(evaluator);

		Algorithm<Solution<T>> algorithm = builder.build();
		algorithm.run();
		Solution<T> best = algorithm.getResult();
		evaluator.shutdown();

		return best.variables().get(0);
	}

	public static void main(String[] args) {

		int n = 10;
		Rastrigin rastrigin = new Rastrigin(n);
		ErrorLoggingFunction<double[]> error = new ErrorLoggingFunction<>(rastrigin);
		Supplier<double[]> genertor = new Supplier<double[]>() {

			@Override
			public double[] get() {
				Random random = new Random();
				double[] array = new double[n];
				for (int i = 0; i < n; i++) {
					array[i] = random.nextGaussian();
				}
				return array;
			}
		};

		Problem<Solution<double[]>> problem = new WrappedCustomProblem<double[]>(error, genertor);

		BinaryOperator<double[]> crossover = new BinaryOperator<double[]>() {
			@Override
			public double[] apply(double[] a, double[] b) {
				double[] c = new double[n];
				for (int i = 0; i < n; i++) {
					c[i] = (a[i] + b[i]) / 2;
				}
				return c;
			}
		};
		UnaryOperator<double[]> mutation = new UnaryOperator<double[]>() {

			@Override
			public double[] apply(double[] x) {
				Random random = new Random();
				double[] array = new double[n];
				for (int i = 0; i < n; i++) {
					array[i] = x[i] + random.nextGaussian() * 0.1;
				}
				return array;
			}
		};
		System.out.println(Arrays.toString(runGA(problem, crossover, mutation, 2000, 4)));

		double[] yData = error.log.stream().mapToDouble(d -> d).toArray();
		double[] xData = IntStream.range(0, yData.length).asDoubleStream().toArray();

		XYChart chart = QuickChart.getChart("Sample Chart", "Time", "Error", "y(t)", xData, yData);
		new SwingWrapper<XYChart>(chart).displayChart();

	}
}

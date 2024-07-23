package numeric;

import java.util.Arrays;
import java.util.stream.IntStream;

import org.knowm.xchart.QuickChart;
import org.knowm.xchart.SwingWrapper;
import org.knowm.xchart.XYChart;
import org.uma.jmetal.algorithm.Algorithm;
import org.uma.jmetal.algorithm.singleobjective.geneticalgorithm.GeneticAlgorithmBuilder;
import org.uma.jmetal.algorithm.singleobjective.particleswarmoptimization.StandardPSO2011;
import org.uma.jmetal.operator.crossover.CrossoverOperator;
import org.uma.jmetal.operator.crossover.impl.SBXCrossover;
import org.uma.jmetal.operator.mutation.MutationOperator;
import org.uma.jmetal.operator.mutation.impl.PolynomialMutation;
import org.uma.jmetal.problem.doubleproblem.DoubleProblem;
import org.uma.jmetal.solution.doublesolution.DoubleSolution;
import org.uma.jmetal.util.evaluator.SolutionListEvaluator;
import org.uma.jmetal.util.evaluator.impl.MultiThreadedSolutionListEvaluator;

import common.ErrorLoggingFunction;

public class Example {

	public static double[] runPSO(DoubleProblem problem, int limit, int numberOfCores) {
		SolutionListEvaluator<DoubleSolution> evaluator = 
				new MultiThreadedSolutionListEvaluator<DoubleSolution>(numberOfCores);

		int swarmSize = 10 + (int) (2 * Math.sqrt(problem.getNumberOfVariables()));
		int maxIterations = limit / swarmSize;

		Algorithm<DoubleSolution> algorithm = 
				new StandardPSO2011(problem, swarmSize, maxIterations, 3, evaluator);
		algorithm.run();
		DoubleSolution best = algorithm.getResult();
		evaluator.shutdown();

		return WrappedDoubleProblem.toArray(best);
	}

	public static double[] runGA(DoubleProblem problem, int limit, int numberOfCores) {
		SolutionListEvaluator<DoubleSolution> evaluator = 
				new MultiThreadedSolutionListEvaluator<DoubleSolution>(numberOfCores);

		CrossoverOperator<DoubleSolution> crossoverOperator = new SBXCrossover(0.9, 20.0);
		MutationOperator<DoubleSolution> mutationOperator = new PolynomialMutation(0.9, 20.0);

		GeneticAlgorithmBuilder<DoubleSolution> builder = 
				new GeneticAlgorithmBuilder<DoubleSolution>(problem, crossoverOperator, mutationOperator);
		builder.setMaxEvaluations(limit);
		builder.setSolutionListEvaluator(evaluator);

		Algorithm<DoubleSolution> algorithm = builder.build();
		algorithm.run();
		DoubleSolution best = algorithm.getResult();
		evaluator.shutdown();

		return best.variables().stream().mapToDouble(d -> d).toArray();
	}

	public static void main(String[] args) {

		int n = 10;
		Rastrigin rastrigin = new Rastrigin(n);
		ErrorLoggingFunction<double[]> error = new ErrorLoggingFunction<>(rastrigin);
		DoubleProblem problem = new WrappedDoubleProblem(n, error, -5.12, +5.12);

		//	System.out.println(Arrays.toString(runGA(problem, 2000, 4)));
		 System.out.println(Arrays.toString(runPSO(problem, 2000, 4)));

		double[] yData = error.log.stream().mapToDouble(d -> d).toArray();
		double[] xData = IntStream.range(0, yData.length).asDoubleStream().toArray();

		XYChart chart = QuickChart.getChart("Sample Chart", "Time", "Error", "y(t)", xData, yData);
		new SwingWrapper<XYChart>(chart).displayChart();

	}
}

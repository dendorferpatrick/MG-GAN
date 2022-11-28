from test_tube import HyperOptArgumentParser


def get_parser():
    parser = HyperOptArgumentParser(strategy="grid_search")

    parser.add_argument("--name", type=str, default="test")
    parser.add_argument("--log_dir", type=str, default="../logs/")
    parser.add_argument(
        "--dataset",
        type=str,
        default="stanford_synthetic",
        choices=[
            "hotel",
            "eth",
            "zara1",
            "zara2",
            "univ",
            "motsynth", 
            "social_stanford_synthetic",
            "stanford",
            "gofp",
        ],
    )
    parser.add_argument("--gpus", type=str, default="0")
    parser.add_argument("--workers", type=int, default=0)
    parser.add_argument("--batch_size", type=int, default=8)
    parser.opt_list(
        "--beta1", type=float, default=0.5, options=[0.1, 0.5, 0.9], tunable=False
    )
    parser.add_argument("--load_semantic_map", action="store_true")
    parser.add_argument("--l2_loss_weight", type=float, default=1.0)
    parser.add_argument("--clf_loss_weight", type=float, default=1.0)
    parser.add_argument("--pi_net_loss_weight", type=float, default=1.0)
    parser.add_argument("--epochs", type=int, default=500)
    parser.add_argument("--clipping_threshold_d", type=int, default=100)
    parser.add_argument("--clipping_threshold_g", type=int, default=500)
    parser.add_argument("--num_gen_steps", type=int, default=1)
    parser.add_argument(
        "--inp_format", choices=["rel", "abs", "abs_rel"], default="rel"
    )
    parser.add_argument("--keep_gen_steps", type=int, default=0)
    parser.add_argument("--top_k_test", type=int, default=10)
    parser.add_argument("--val_every", type=int, default=1)
    parser.add_argument("--save_every", type=int, default=5)
    parser.add_argument("--num_unrolling_steps", type=int, default=0)
    parser.add_argument("--debug", action="store_true")
    parser.add_argument("--n_social_modules", type=int, default=1)
    parser.add_argument("--g_lr", type=float, default=1e-3)
    parser.add_argument("--d_lr", type=float, default=1e-3)
    parser.add_argument("--sigma", type=float, default=1.0)
    parser.add_argument(
        "--gan_type",
        type=str,
        choices=["probgan", "mgan", "infogan", "gan"],
        default="mgan",
    )
    parser.add_argument(
        "--experiment",
        type=str,
        choices=[
            "multi_generator",
            "discrete",
        ],
        default="multi_generator",
    )
    parser.add_argument("--pool_type", type=str, default="sways")
    parser.add_argument("--global_disc", type=int, default=1)
    parser.add_argument("--unconditional", action="store_true")
    parser.add_argument("--augment", type=int, default=1)
    parser.add_argument("--noise_dim", type=int, default=8)
    parser.add_argument("--h_dim", type=int, default=32)
    parser.add_argument("--grid_size", type=int, default=16)
    parser.add_argument("--decoder_h_dim", type=int, default=32)
    parser.add_argument("--num_samples", type=int, default=10)
    parser.add_argument("--num_expectation_samples", type=int, default=1)
    parser.add_argument("--pred_len", type=int, default=12)
    parser.add_argument("--obs_len", type=int, default=8)
    parser.add_argument(
        "--weighting_target",
        type=str,
        choices=["l2", "disc_scores", "endpoint", "mgan", "ml", "none"],
        default="ml",
    )

    """ Tunable parameters """
    parser.opt_list(
        "--l2_loss_type",
        type=str,
        options=["none", "min_z", "min_g_z", "min_g_min_z", "mse"],
        default="min_g_z",
        tunable=False,
    )
    parser.opt_list(
        "--num_gens", type=int, options=[2, 3, 4, 5], default=1, tunable=True
    )
    parser.opt_list(
        "--l2_decay_rate", type=float, options=[1, 0.99, 0.9], default=1, tunable=False
    )
    parser.add_argument("--checkpoint", type=str)

    """
    Hyper-parameter for Stochastic Gradient Hamiltonian Monte Carlo
    """
    parser.opt_list(
        "--sghmc_alpha",
        default=0.01,
        type=float,
        dest="sghmc_alpha",
        help="number of generators",
        options=[0.1, 0.01, 0.001],
        tunable=False,
    )
    parser.add_argument(
        "--g_noise_loss_lambda", default=3e-2, type=float, dest="g_noise_loss_lambda"
    )
    parser.add_argument(
        "--d_noise_loss_lambda", default=3e-2, type=float, dest="d_noise_loss_lambda"
    )
    parser.add_argument(
        "--d_hist_loss_lambda", default=1.0, type=float, dest="d_hist_loss_lambda"
    )

    """
    GAN objectives
    NS: original GAN (Non-saturating version)
    MM: original GAN (Min-max version)
    W: Wasserstein GAN
    LS: Least-Square GAN
    """
    parser.opt_list(
        "--gan_obj",
        default="NS",
        type=str,
        dest="gan_obj",
        options=["NS", "MM", "LS", "W"],
        tunable=False,
    )

    return parser

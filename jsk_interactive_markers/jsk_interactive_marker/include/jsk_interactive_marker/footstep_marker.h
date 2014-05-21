// -*- mode: c++ -*-

#include <ros/ros.h>
#include <interactive_markers/interactive_marker_server.h>

#include <interactive_markers/menu_handler.h>
#include <jsk_interactive_marker/SetPose.h>
#include <jsk_interactive_marker/MarkerSetPose.h>
#include <interactive_markers/menu_handler.h>

#include <geometry_msgs/PointStamped.h>

#include <tf/transform_listener.h>
#include <actionlib/client/simple_action_client.h>
#include <jsk_footstep_msgs/PlanFootstepsAction.h>
#include <jsk_footstep_msgs/ExecFootstepsAction.h>
#include <geometry_msgs/Polygon.h>
#include <std_msgs/UInt8.h>
#include <std_msgs/Empty.h>

class FootstepMarker {
public:
  FootstepMarker();
  virtual ~FootstepMarker();
  void updateInitialFootstep();
protected:
  void initializeInteractiveMarker();
  void processFeedbackCB(const visualization_msgs::InteractiveMarkerFeedbackConstPtr &feedback);
  void menuFeedbackCB(const visualization_msgs::InteractiveMarkerFeedbackConstPtr &feedback);
  void moveMarkerCB(const geometry_msgs::PoseStamped::ConstPtr& msg);
  void menuCommandCB(const std_msgs::UInt8::ConstPtr& msg);
  void executeCB(const std_msgs::Empty::ConstPtr& msg);
  void processMenuFeedback(uint8_t id);
  geometry_msgs::Polygon computePolygon(uint8_t leg);
  void snapLegs();
  geometry_msgs::Pose computeLegTransformation(uint8_t leg);
  geometry_msgs::Pose getFootstepPose(bool leftp);
  void planIfPossible();
  void resetLegPoses();
  
  // read a geometry_msgs/pose from the parameter specified.
  // the format of the parameter is [x, y, z, xx, yy, zz, ww].
  // where x, y and z means position and xx, yy, zz and ww means
  // orientation.
  void readPoseParam(ros::NodeHandle& pnh, const std::string param,
                     tf::Transform& offset);

  // execute footstep
  // sending action goal to footstep controller
  void executeFootstep();

  visualization_msgs::Marker makeFootstepMarker(geometry_msgs::Pose pose);
  
  boost::shared_ptr<interactive_markers::InteractiveMarkerServer> server_;
  interactive_markers::MenuHandler menu_handler_;
  double foot_size_x_;
  double foot_size_y_;
  double foot_size_z_;
  double footstep_margin_;
  std::string marker_frame_id_;
  geometry_msgs::PoseStamped marker_pose_;
  ros::Subscriber move_marker_sub_;
  ros::Subscriber menu_command_sub_;
  ros::Subscriber exec_sub_;
  ros::Publisher footstep_pub_;
  ros::ServiceClient snapit_client_;
  boost::shared_ptr<tf::TransformListener> tf_listener_;
  actionlib::SimpleActionClient<jsk_footstep_msgs::PlanFootstepsAction> ac_;
  actionlib::SimpleActionClient<jsk_footstep_msgs::ExecFootstepsAction> ac_exec_;
  bool use_footstep_planner_;
  bool use_footstep_controller_;
  bool plan_run_;
  bool wait_snapit_server_;
  bool use_initial_footstep_tf_;
  geometry_msgs::Pose lleg_pose_;
  geometry_msgs::Pose rleg_pose_;
  geometry_msgs::Pose lleg_initial_pose_;
  geometry_msgs::Pose rleg_initial_pose_;
  tf::Transform lleg_offset_;
  tf::Transform rleg_offset_;
  std::string lfoot_frame_id_;
  std::string rfoot_frame_id_;

  // footstep plannner result
  jsk_footstep_msgs::PlanFootstepsResult::ConstPtr plan_result_;
};
